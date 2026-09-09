// Audit script: extract all articles info from articles-data.js
const fs = require('fs');
const content = fs.readFileSync('d:/Personal/AntiGravity/Affiliate Marketting/scripts/articles-data.js', 'utf8');

// Find all article objects
const idMatches = [...content.matchAll(/id:\s*(\d+),/g)];
const titleMatches = [...content.matchAll(/title:\s*"([^"]+)"/g)];
const slugMatches = [...content.matchAll(/slug:\s*"([^"]+)"/g)];
const categoryMatches = [...content.matchAll(/category:\s*"([^"]+)"/g)];
const contentHtmlMatches = [...content.matchAll(/contentHtml:\s*`([\s\S]*?)`\s*[\r\n]/g)];

console.log("=== ARTICLE INVENTORY ===");
console.log("Total IDs found:", idMatches.length);
console.log("Total titles found:", titleMatches.length);
console.log("Total contentHtml blocks found:", contentHtmlMatches.length);
console.log("");

for (let i = 0; i < idMatches.length; i++) {
  const id = idMatches[i][1];
  const title = titleMatches[i] ? titleMatches[i][1] : "MISSING";
  const slug = slugMatches[i] ? slugMatches[i][1] : "MISSING";
  const category = categoryMatches[i] ? categoryMatches[i][1] : "MISSING";
  const contentLen = contentHtmlMatches[i] ? contentHtmlMatches[i][1].length : 0;
  
  // Check content quality
  const htmlContent = contentHtmlMatches[i] ? contentHtmlMatches[i][1] : "";
  const hasH2 = (htmlContent.match(/<h2/g) || []).length;
  const hasFAQ = htmlContent.toLowerCase().includes("frequently asked") || htmlContent.toLowerCase().includes("faq");
  const hasTable = htmlContent.includes("<table");
  const hasFormula = htmlContent.includes("font-mono") || htmlContent.includes("ctl-spec-box");
  const hasAuthor = htmlContent.includes("ctl-author-box");
  const hasRelated = htmlContent.toLowerCase().includes("related") || htmlContent.includes("openArticleModal");
  
  const status = contentLen < 5000 ? "⚠️ THIN" : contentLen < 10000 ? "🔶 SHORT" : "✅ FULL";
  
  console.log(`${status} ID ${id}: "${title}"`);
  console.log(`   Slug: ${slug} | Category: ${category}`);
  console.log(`   Content: ${contentLen} chars | H2s: ${hasH2} | FAQ: ${hasFAQ} | Table: ${hasTable} | Formula: ${hasFormula} | Author: ${hasAuthor} | Related: ${hasRelated}`);
  console.log("");
}
