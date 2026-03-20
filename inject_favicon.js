const fs = require('fs');
const path = require('path');
const d = process.cwd();

fs.readdirSync(d).filter(f => f.endsWith('.html')).forEach(f => {
    let c = fs.readFileSync(path.join(d, f), 'utf8');
    
    // If favicon is not already linked:
    if (!c.includes('rel="icon"')) {
        let favTag = '\n    <link rel="icon" type="image/png" href="makertoo-favicon.png" />';
        // Inject into <head>
        c = c.replace(/<\/title>/, '</title>' + favTag);
    }
    
    fs.writeFileSync(path.join(d, f), c);
    console.log('Added favicon link to', f);
});
