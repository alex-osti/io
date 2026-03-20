const fs = require('fs');
const path = require('path');
const d = process.cwd();

fs.readdirSync(d).filter(f => f.endsWith('.html')).forEach(f => {
    let c = fs.readFileSync(path.join(d, f), 'utf8');
    
    // We already moved the aside to bottom on mobile in `fix-mobile.js`.
    // Now we must inject a hamburger button for the MAIN top nav links.
    
    // 1. Grab the top nav links block using regex:
    // This matches the <div class="hidden md:flex items-center gap-10">...</div>
    // or space-x-8 etc.
    let navLinksMatch = c.match(/<div class="hidden md:flex[^>]*>([\s\S]*?)<\/div>/);
    let navLinks = '';
    
    if (navLinksMatch) {
        navLinks = navLinksMatch[1];
        // Make the links bigger and more mobile-app looking:
        navLinks = navLinks
            .replace(/text-sm/g, 'text-2xl py-4 border-b border-outline-variant/10 w-full font-bold')
            .replace(/text-xs lg:text-sm/g, 'text-2xl py-4 border-b border-outline-variant/10 w-full font-bold')
            .replace(/border-b-[0-9][^ ]+/g, '') // strip original bottom borders
            .replace(/pb-1/g, 'text-primary') // make active items primary colored
    }
    
    // 2. Add the Hamburger Menu button if it doesn't exist
    if (!c.includes('toggleMobileMenu()') && c.includes('<div class="hidden md:flex')) {
        c = c.replace(/<div class="hidden md:flex/, 
            `<button onclick="toggleMobileMenu()" class="md:hidden text-on-surface ml-auto mr-4 cursor-pointer hover:bg-surface-bright/20 rounded-lg p-2 transition-colors">
                <span class="material-symbols-outlined text-3xl">menu</span>
            </button>
            <div class="hidden md:flex`
        );
    }

    // 3. Make sure the Logo is properly truncated on mobile
    // c = c.replace(/font-headline truncate max-w-\[50%\] md:max-w-none text-xl md:text-2xl/g, 'font-headline max-w-[65%] sm:max-w-none text-lg sm:text-xl md:text-2xl truncate');
    c = c.replace(/class="text-[^"]+font-black tracking-tighter text-\[#e3e2e8\] font-headline[^"]*"/, 'class="text-lg sm:text-xl md:text-2xl font-black tracking-tighter text-[#e3e2e8] font-headline max-w-[60%] sm:max-w-none truncate"');

    // 4. Inject the Mobile Menu Overlay + JS before </body>
    if (!c.includes('id="mobile-menu"')) {
        let overlayHTML = `
<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 bg-[#0d0e12]/98 backdrop-blur-3xl z-[100] transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col pt-6 px-6 md:hidden">
    <div class="flex justify-between items-center w-full mb-8">
        <div class="text-xl font-black text-primary font-headline">Strateški Meni</div>
        <button onclick="toggleMobileMenu()" class="text-on-surface p-2 hover:bg-surface-bright/20 rounded-full transition-colors">
            <span class="material-symbols-outlined text-3xl">close</span>
        </button>
    </div>
    
    <div class="flex flex-col items-start w-full border-t border-white/5 pt-6 text-on-surface">
        ${navLinks}
    </div>
    
    <div class="mt-auto pb-12 w-full flex justify-center">
        <div class="flex items-center gap-2 px-6 py-4 bg-tertiary/10 border border-tertiary/20 rounded-xl shadow-[0_0_20px_rgba(102,221,139,0.1)]">
            <span class="h-3 w-3 rounded-full bg-tertiary animate-pulse"></span>
            <span class="text-tertiary font-bold text-sm uppercase tracking-widest">Sistem Deluje</span>
        </div>
    </div>
</div>

<script>
    function toggleMobileMenu() {
        const menu = document.getElementById('mobile-menu');
        menu.classList.toggle('translate-x-full');
        document.body.classList.toggle('overflow-hidden'); // Prevent background scroll
    }
</script>
</body>`;
        c = c.replace('</body>', overlayHTML);
    }

    fs.writeFileSync(path.join(d, f), c);
    console.log('Injected mobile menu into', f);
});
