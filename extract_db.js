const fs = require('fs');
const path = require('path');

function parseSqlValues(str) {
  const rows = [];
  let inString = false;
  let escape = false;
  let currentVal = '';
  let row = [];
  let inRow = false;

  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    if (escape) {
      currentVal += char;
      escape = false;
      continue;
    }
    if (char === '\\') {
      escape = true;
      continue;
    }
    if (char === "'") {
      inString = !inString;
      continue;
    }
    if (inString) {
      currentVal += char;
      continue;
    }

    if (char === '(' && !inRow) {
      inRow = true;
      row = [];
      currentVal = '';
      continue;
    }
    if (char === ')' && inRow) {
      row.push(currentVal.trim() === 'NULL' ? null : currentVal.trim());
      rows.push(row);
      inRow = false;
      currentVal = '';
      continue;
    }
    if (char === ',' && inRow) {
      row.push(currentVal.trim() === 'NULL' ? null : currentVal.trim());
      currentVal = '';
      continue;
    }
    if (inRow) {
      currentVal += char;
    }
  }
  return rows;
}

const sqlPath = 'c:/Users/User/Desktop/qclarxeq_qclab.sql';
console.log('Reading SQL dump...');
const content = fs.readFileSync(sqlPath, 'utf8');

function extractTable(tableName) {
  const regex = new RegExp('INSERT INTO `' + tableName + '` [^;]*?;', 'g');
  let match;
  const allRows = [];
  
  // Use regex to find INSERT INTO `tableName` (`col1`, ...) VALUES
  const prefix = 'INSERT INTO `' + tableName + '`';
  let pos = 0;
  while ((pos = content.indexOf(prefix, pos)) !== -1) {
    const valuesIdx = content.indexOf('VALUES', pos);
    if (valuesIdx === -1) break;
    let endIdx = valuesIdx + 6;
    let inStr = false;
    let esc = false;
    while (endIdx < content.length) {
      const c = content[endIdx];
      if (esc) {
        esc = false;
        endIdx++;
        continue;
      }
      if (c === '\\') {
        esc = true;
        endIdx++;
        continue;
      }
      if (c === "'") {
        inStr = !inStr;
        endIdx++;
        continue;
      }
      if (c === ';' && !inStr) {
        break;
      }
      endIdx++;
    }
    const valuesPart = content.slice(valuesIdx + 6, endIdx);
    const rows = parseSqlValues(valuesPart);
    allRows.push(...rows);
    pos = endIdx + 1;
  }
  return allRows;
}

const catCols = ['id', 'old_id', 'name', 'slug', 'image', 'meta_title', 'meta_keywords', 'meta_description', 'tagline', 'description', 'is_menu', 'parent_id', 'type', 'sorting', 'status', 'created_at', 'updated_at', 'deleted_at'];
const prodCols = ['id', 'unit_id', 'category_id', 'sub_category_id', 'child_category_id', 'brand_id', 'item_id', 'name', 'slug', 'thumbnail', 'meta_title', 'meta_key', 'meta_description', 'short_description', 'sell_rate', 'is_special', 'sorting', 'status', 'total_view', 'created_at', 'updated_at', 'deleted_at'];
const imgCols = ['id', 'product_id', 'variation_id', 'image', 'alt_name', 'status', 'created_at', 'updated_at', 'deleted_at'];
const descCols = ['id', 'data_id', 'reference_table', 'details_segment', 'type', 'status', 'created_at', 'updated_at', 'deleted_at'];

console.log('Extracting categories...');
const rawCats = extractTable('categories');
console.log(`Found ${rawCats.length} raw categories`);

console.log('Extracting products...');
const rawProds = extractTable('products');
console.log(`Found ${rawProds.length} raw products`);

console.log('Extracting product images...');
const rawImgs = extractTable('product_images');
console.log(`Found ${rawImgs.length} raw product images`);

console.log('Extracting descriptions...');
const rawDescs = extractTable('descriptions');
console.log(`Found ${rawDescs.length} raw descriptions`);

const categories = rawCats.map(r => {
  const obj = {};
  catCols.forEach((col, idx) => { obj[col] = r[idx]; });
  return obj;
});

const products = rawProds.map(r => {
  const obj = {};
  prodCols.forEach((col, idx) => { obj[col] = r[idx]; });
  return obj;
});

const productImages = rawImgs.map(r => {
  const obj = {};
  imgCols.forEach((col, idx) => { obj[col] = r[idx]; });
  return obj;
});

const descriptions = rawDescs.map(r => {
  const obj = {};
  descCols.forEach((col, idx) => { obj[col] = r[idx]; });
  return obj;
});

// Map product descriptions (reference_table === 'products')
const prodDescMap = {};
descriptions.forEach(d => {
  if (d.reference_table === 'products') {
    if (!prodDescMap[d.data_id]) prodDescMap[d.data_id] = [];
    prodDescMap[d.data_id].push(d);
  }
});

// Map product images
const prodImgMap = {};
productImages.forEach(img => {
  if (!prodImgMap[img.product_id]) prodImgMap[img.product_id] = [];
  prodImgMap[img.product_id].push(img);
});

// Attach images and descriptions to products
const fullProducts = products.map(p => {
  return {
    ...p,
    gallery_images: (prodImgMap[p.id] || []).map(i => i.image),
    details: (prodDescMap[p.id] || []).map(d => ({ type: d.type, content: d.details_segment }))
  };
});

const extraTables = ['brands', 'site_infos', 'sliders', 'services', 'service_categories', 'industries', 'industry_categories', 'projects', 'clients'];
const extraData = {};
extraTables.forEach(tbl => {
  const raw = extractTable(tbl);
  console.log(`Found ${raw.length} records for ${tbl}`);
  extraData[tbl] = raw;
});

const output = {
  scraped_at: new Date().toISOString(),
  total_categories: categories.length,
  total_products: fullProducts.length,
  categories: categories,
  products: fullProducts,
  extras: extraData
};

fs.writeFileSync('c:/Users/User/Desktop/qc/scraped_database.json', JSON.stringify(output, null, 2));
console.log('Successfully saved to c:/Users/User/Desktop/qc/scraped_database.json');

