import panflute as pf

def html_comments_to_text(elem, doc):
    if isinstance(elem, pf.RawInline) and elem.format == 'html':
        if "<!--" in elem.text and "-->" in elem.text:
            return pf.Str(elem.text)

def main(doc=None):
    return pf.run_filter(html_comments_to_text, doc=doc)

if __name__ == "__main__":
    main()
