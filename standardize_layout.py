import os
import re

directory = r'c:\Users\david\io-value'
files = ['index.html', 'summary.html', 'forth.html', 'second.html', 'third.html', 'sixth.html', 'seventh.html', 'seo.html']

# Standard sidebar content (we will update active link per file)
sidebar_template = '''
    <aside class="hidden md:flex md:flex-col fixed md:left-0 md:top-24 md:bottom-0 md:w-20 md:hover:w-64 items-start justify-start md:py-8 bg-[#121317] md:border-r border-white/5 z-40 group md:overflow-hidden transition-all duration-300 bg-gradient-to-r from-[#1a1b20] to-transparent shadow-2xl">
        <div class="flex flex-col gap-8 w-full px-4">
            <a class="flex items-center gap-4 py-3 px-3 ACTIVE_LINK_summary text-[#c4c6cc] opacity-60 hover:opacity-100 hover:text-primary transition-all duration-500 ease-out" href="index.html">
                <span class="material-symbols-outlined" data-icon="analytics">analytics</span>
                <span class="opacity-0 group-hover:opacity-100 font-medium text-xs font-['Inter'] whitespace-nowrap">Povzetek stanja</span>
            </a>
            <a class="flex items-center gap-4 py-3 px-3 ACTIVE_LINK_sixth text-[#c4c6cc] opacity-60 hover:opacity-100 hover:text-primary transition-all duration-500 ease-out" href="sixth.html">
                <span class="material-symbols-outlined" data-icon="dns">dns</span>
                <span class="opacity-0 group-hover:opacity-100 font-medium text-xs font-['Inter'] whitespace-nowrap">Infrastruktura</span>
            </a>
            <a class="flex items-center gap-4 py-3 px-3 ACTIVE_LINK_seventh text-[#c4c6cc] opacity-60 hover:opacity-100 hover:text-primary transition-all duration-500 ease-out" href="seventh.html">
                <span class="material-symbols-outlined" data-icon="hub">hub</span>
                <span class="opacity-0 group-hover:opacity-100 font-medium text-xs font-['Inter'] whitespace-nowrap">Avtomatizacija</span>
            </a>
            <a class="flex items-center gap-4 py-3 px-3 ACTIVE_LINK_seo text-[#c4c6cc] opacity-60 hover:opacity-100 hover:text-primary transition-all duration-500 ease-out" href="seo.html">
                <span class="material-symbols-outlined" data-icon="trending_up">trending_up</span>
                <span class="opacity-0 group-hover:opacity-100 font-medium text-xs font-['Inter'] whitespace-nowrap">SEO zmogljivost</span>
            </a>
            <a class="flex items-center gap-4 py-3 px-3 ACTIVE_LINK_forth text-[#c4c6cc] opacity-60 hover:opacity-100 hover:text-primary transition-all duration-500 ease-out" href="forth.html">
                <span class="material-symbols-outlined" data-icon="payments">payments</span>
                <span class="opacity-0 group-hover:opacity-100 font-medium text-xs font-['Inter'] whitespace-nowrap">Vrednost projekta</span>
            </a>
        </div>
        <div class="mt-auto px-4 pb-8 w-full">
            <div class="w-full bg-primary/10 border border-primary/20 text-primary text-[10px] py-3 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap text-center font-bold tracking-widest">
                VERIFIED 2026
            </div>
        </div>
    </aside>
'''

def patch_file(filename, content):
    # 1. Standardize Sidebar
    current_key = filename.replace('.html', '')
    if current_key == 'index': current_key = 'summary'
    
    current_sidebar = sidebar_template
    # Mark active link
    active_class = "bg-primary/10 text-primary opacity-100 rounded-r-full"
    for key in ['summary', 'sixth', 'seventh', 'seo', 'forth']:
        if key == current_key:
            current_sidebar = current_sidebar.replace(f'ACTIVE_LINK_{key}', active_class)
        else:
            current_sidebar = current_sidebar.replace(f'ACTIVE_LINK_{key}', '')
    
    aside_pattern = r'<aside[^>]*>.*?</aside>'
    content = re.sub(aside_pattern, current_sidebar, content, flags=re.DOTALL)
    
    # 2. Standardize Main Container
    # We want <main class="md:ml-20 pt-24 md:pt-32 pb-16">
    # And then wrap all contents in <div class="max-w-7xl mx-auto px-4 md:px-12 lg:px-24">
    
    main_match = re.search(r'<main[^>]*>(.*?)</main>', content, flags=re.DOTALL)
    if main_match:
        inner_content = main_match.group(1)
        # Remove any existing outer padding/max-width from inner tags to avoid conflicts
        inner_content = re.sub(r'max-w-7xl mx-auto', '', inner_content)
        # Standardized main structure
        new_main = f'''
    <main class="md:ml-20 pt-24 md:pt-32 pb-16">
        <div class="max-w-7xl mx-auto px-4 md:px-12 lg:px-24">
            {inner_content.strip()}
        </div>
    </main>'''
        content = re.sub(r'<main[^>]*>.*?</main>', new_main, content, flags=re.DOTALL)

    return content

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = patch_content_final(filename, content) # We use the logic defined above
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# wait, I made a mistake in the loop naming.
# Re-writing the loop properly below.
