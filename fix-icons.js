const fs = require('fs');
const path = require('path');
const d = process.cwd();

fs.readdirSync(d).filter(f => f.endsWith('.html')).forEach(f => {
    let c = fs.readFileSync(path.join(d, f), 'utf8');
    
    // Fix broken trending_up spans
    // It currently looks like: href="seo.html">trending_up</span>
    // Needs to be: href="seo.html"><span class="material-symbols-outlined" data-icon="trending_up">trending_up</span>
    
    c = c.replace(/href="seo\.html">trending_up<\/span>/g, 'href="seo.html"><span class="material-symbols-outlined" data-icon="trending_up">trending_up</span>');
    
    // Also check for similar broken one in mobile-menu injection if any
    c = c.replace(/>trending_up<\/span>/g, '><span class="material-symbols-outlined" data-icon="trending_up">trending_up</span>');
    // Ensure it doesn't double wrap if it was correct (safe regex)
    c = c.replace(/<span class="material-symbols-outlined" data-icon="trending_up"><span class="material-symbols-outlined" data-icon="trending_up">trending_up<\/span><\/span>/g, '<span class="material-symbols-outlined" data-icon="trending_up">trending_up</span>');

    fs.writeFileSync(path.join(d, f), c);
    console.log('Fixed icon tags in', f);
});
