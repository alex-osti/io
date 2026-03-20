const fs = require('fs');
const path = require('path');
const d = process.cwd();

fs.readdirSync(d).filter(f => f.endsWith('.html')).forEach(f => {
    let c = fs.readFileSync(path.join(d, f), 'utf8');
    c = c.replace(/href="first\.html"/g, 'href="index.html"');
    fs.writeFileSync(path.join(d, f), c);
    console.log('Updated links in', f);
});
