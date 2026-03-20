"""
Unify ALL pages navigation to use fifth.html as home (Pregled stanja).
Updates: mobile overlay, desktop top nav (5 links with correct labels), aside nav hrefs.
"""
import re

BASE = 'C:/Users/david/io-value/'

INACTIVE = 'font-headline text-sm tracking-wide uppercase font-bold text-[#c4c6cc] hover:text-[#e3e2e8] transition-colors duration-300'
ACTIVE   = 'font-headline text-sm tracking-wide uppercase font-bold text-[#00daf3] border-b-2 border-[#00daf3] pb-1'

UNIFIED_NAV = [
    ('fifth.html',   'Pregled stanja'),
    ('sixth.html',   'Infrastruktura'),
    ('seventh.html', 'Avtomatizacija'),
    ('seo.html',     'SEO'),
    ('forth.html',   'Vrednost'),
]

ACTIVE_PAGE = {
    'index.html':   None,
    'second.html':  None,
    'third.html':   None,
    'forth.html':   'forth.html',
    'fifth.html':   'fifth.html',
    'sixth.html':   'sixth.html',
    'seventh.html': 'seventh.html',
    'seo.html':     'seo.html',
}

UNIFIED_OVERLAY_ITEMS = [
    ('analytics',   'fifth.html',   'Pregled stanja'),
    ('dns',         'sixth.html',   'Infrastruktura'),
    ('hub',         'seventh.html', 'Avtomatizacija'),
    ('trending_up', 'seo.html',     'SEO'),
    ('payments',    'forth.html',   'Vrednost'),
]


def build_overlay(filename):
    active_page = ACTIVE_PAGE[filename]
    nav_items = []
    for icon, href, label in UNIFIED_OVERLAY_ITEMS:
        is_active = href == active_page
        if is_active:
            cls = 'flex items-center gap-4 px-4 py-3.5 rounded-xl bg-primary/10 text-primary transition-all duration-200'
            arrow = '\n                <span class="material-symbols-outlined text-sm shrink-0">chevron_right</span>'
        else:
            cls = 'flex items-center gap-4 px-4 py-3.5 rounded-xl text-on-surface-variant hover:text-on-surface hover:bg-white/5 transition-all duration-200'
            arrow = ''
        nav_items.append(
            '            <a href="' + href + '" class="' + cls + '">\n'
            '                <span class="material-symbols-outlined text-xl shrink-0">' + icon + '</span>\n'
            '                <span class="font-bold text-sm uppercase tracking-wide flex-1">' + label + '</span>' + arrow + '\n'
            '            </a>'
        )
    nav_html = '\n'.join(nav_items)
    return (
        '<!-- Mobile Menu -->\n'
        '<div id="mobile-menu" class="fixed inset-0 z-[100] md:hidden" aria-hidden="true" style="pointer-events:none">\n'
        '    <div id="mm-backdrop" onclick="toggleMobileMenu()" class="absolute inset-0 bg-black/70 backdrop-blur-sm opacity-0 transition-opacity duration-300 ease-out cursor-pointer"></div>\n'
        '    <div id="mm-drawer" class="absolute right-0 top-0 h-full w-[280px] bg-[#0d0e12] border-l border-white/5 flex flex-col translate-x-full transition-transform duration-300 ease-out shadow-2xl">\n'
        '        <div class="flex items-center justify-between px-5 py-4 border-b border-white/5">\n'
        '            <div>\n'
        '                <div class="text-primary font-bold text-[10px] uppercase tracking-widest mb-0.5">Navigacija</div>\n'
        '                <div class="text-on-surface font-black text-base" style="font-family:Manrope,sans-serif">MakerToo/Io-Natural</div>\n'
        '            </div>\n'
        '            <button onclick="toggleMobileMenu()" class="p-2 -mr-2 text-on-surface-variant hover:text-on-surface transition-colors rounded-lg hover:bg-white/5">\n'
        '                <span class="material-symbols-outlined">close</span>\n'
        '            </button>\n'
        '        </div>\n'
        '        <nav class="flex-1 px-3 py-4 space-y-1 overflow-y-auto">\n'
        + nav_html + '\n'
        '        </nav>\n'
        '        <div class="px-5 py-4 border-t border-white/5">\n'
        '            <div class="flex items-center gap-2.5 px-4 py-3 bg-tertiary/10 border border-tertiary/20 rounded-xl">\n'
        '                <span class="h-2 w-2 rounded-full bg-tertiary animate-pulse"></span>\n'
        '                <span class="text-tertiary font-bold text-xs uppercase tracking-widest">Sistem deluje</span>\n'
        '            </div>\n'
        '        </div>\n'
        '    </div>\n'
        '</div>\n\n'
        '<script>\n'
        'function toggleMobileMenu(){\n'
        "    var o=document.getElementById('mobile-menu'),b=document.getElementById('mm-backdrop'),d=document.getElementById('mm-drawer'),open=o.dataset.open==='1';\n"
        "    if(!open){o.style.pointerEvents='auto';o.setAttribute('aria-hidden','false');o.dataset.open='1';document.body.style.overflow='hidden';requestAnimationFrame(function(){b.style.opacity='1';d.style.transform='translateX(0)';});}\n"
        "    else{b.style.opacity='0';d.style.transform='translateX(100%)';document.body.style.overflow='';setTimeout(function(){o.style.pointerEvents='none';o.setAttribute('aria-hidden','true');o.dataset.open='0';},300);}\n"
        '}\n'
        "document.addEventListener('keydown',function(e){if(e.key==='Escape'&&document.getElementById('mobile-menu').dataset.open==='1')toggleMobileMenu();});\n"
        '</script>'
    )


def build_desktop_nav_block(filename):
    """Replace the entire hidden md:flex nav links div."""
    active_page = ACTIVE_PAGE[filename]
    links = []
    for href, label in UNIFIED_NAV:
        cls = ACTIVE if href == active_page else INACTIVE
        links.append('            <a class="' + cls + '" href="' + href + '">' + label + '</a>')
    return (
        '<div class="hidden md:flex items-center gap-10">\n'
        + '\n'.join(links)
        + '\n        </div>'
    )


def fix_aside_hrefs(content):
    """Update href values inside <aside>...</aside> only."""
    def replacer(m):
        inner = m.group(2)
        inner = inner.replace('href="index.html"', 'href="fifth.html"')
        inner = inner.replace('href="second.html"', 'href="sixth.html"')
        inner = inner.replace('href="third.html"', 'href="seventh.html"')
        return m.group(1) + inner + m.group(3)
    return re.sub(r'(<aside\b[^>]*>)([\s\S]*?)(</aside>)', replacer, content, flags=re.DOTALL)


ALL_PAGES = list(ACTIVE_PAGE.keys())

for filename in ALL_PAGES:
    path = BASE + filename
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. Replace mobile overlay
    new = re.sub(
        r'(<!-- Mobile Menu[^\n]*\n\s*)?<div id="mobile-menu".*?</script>',
        build_overlay(filename),
        content, flags=re.DOTALL
    )
    if new != content:
        content = new
        print('  [overlay] ' + filename)

    # 2. Replace desktop top nav links block (the hidden md:flex div)
    new = re.sub(
        r'<div class="hidden md:flex items-center[^"]*">[\s\S]*?</div>',
        build_desktop_nav_block(filename),
        content
    )
    if new != content:
        content = new
        print('  [desktop-nav] ' + filename)

    # 3. Fix aside hrefs (scoped to <aside> block, safe from CTA contamination)
    new = fix_aside_hrefs(content)
    if new != content:
        content = new
        print('  [aside] ' + filename)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('[SAVED] ' + filename)
    else:
        print('[UNCHANGED] ' + filename)

print('Done.')
