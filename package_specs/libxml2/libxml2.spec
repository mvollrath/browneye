Name:       libxml2
Version:    2.9.9
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
%configure  --disable-static \
            --with-history   \
            --with-python=/usr/bin/python3
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint
/usr/include/libxml2/libxml/DOCBparser.h
/usr/include/libxml2/libxml/HTMLparser.h
/usr/include/libxml2/libxml/HTMLtree.h
/usr/include/libxml2/libxml/SAX.h
/usr/include/libxml2/libxml/SAX2.h
/usr/include/libxml2/libxml/c14n.h
/usr/include/libxml2/libxml/catalog.h
/usr/include/libxml2/libxml/chvalid.h
/usr/include/libxml2/libxml/debugXML.h
/usr/include/libxml2/libxml/dict.h
/usr/include/libxml2/libxml/encoding.h
/usr/include/libxml2/libxml/entities.h
/usr/include/libxml2/libxml/globals.h
/usr/include/libxml2/libxml/hash.h
/usr/include/libxml2/libxml/list.h
/usr/include/libxml2/libxml/nanoftp.h
/usr/include/libxml2/libxml/nanohttp.h
/usr/include/libxml2/libxml/parser.h
/usr/include/libxml2/libxml/parserInternals.h
/usr/include/libxml2/libxml/pattern.h
/usr/include/libxml2/libxml/relaxng.h
/usr/include/libxml2/libxml/schemasInternals.h
/usr/include/libxml2/libxml/schematron.h
/usr/include/libxml2/libxml/threads.h
/usr/include/libxml2/libxml/tree.h
/usr/include/libxml2/libxml/uri.h
/usr/include/libxml2/libxml/valid.h
/usr/include/libxml2/libxml/xinclude.h
/usr/include/libxml2/libxml/xlink.h
/usr/include/libxml2/libxml/xmlIO.h
/usr/include/libxml2/libxml/xmlautomata.h
/usr/include/libxml2/libxml/xmlerror.h
/usr/include/libxml2/libxml/xmlexports.h
/usr/include/libxml2/libxml/xmlmemory.h
/usr/include/libxml2/libxml/xmlmodule.h
/usr/include/libxml2/libxml/xmlreader.h
/usr/include/libxml2/libxml/xmlregexp.h
/usr/include/libxml2/libxml/xmlsave.h
/usr/include/libxml2/libxml/xmlschemas.h
/usr/include/libxml2/libxml/xmlschemastypes.h
/usr/include/libxml2/libxml/xmlstring.h
/usr/include/libxml2/libxml/xmlunicode.h
/usr/include/libxml2/libxml/xmlversion.h
/usr/include/libxml2/libxml/xmlwriter.h
/usr/include/libxml2/libxml/xpath.h
/usr/include/libxml2/libxml/xpathInternals.h
/usr/include/libxml2/libxml/xpointer.h
/usr/lib64/cmake/libxml2/libxml2-config.cmake
/usr/lib64/libxml2.la
/usr/lib64/libxml2.so
/usr/lib64/libxml2.so.2
/usr/lib64/libxml2.so.2.9.9
/usr/lib64/pkgconfig/libxml-2.0.pc
/usr/lib64/python3.7/site-packages/drv_libxml2.py
/usr/lib64/python3.7/site-packages/libxml2.py
/usr/lib64/python3.7/site-packages/libxml2mod.la
/usr/lib64/python3.7/site-packages/libxml2mod.so
/usr/lib64/xml2Conf.sh
/usr/share/aclocal/libxml.m4
/usr/share/doc/libxml2-2.9.9/Copyright
/usr/share/doc/libxml2-2.9.9/examples/testHTML.c
/usr/share/doc/libxml2-2.9.9/examples/testSAX.c
/usr/share/doc/libxml2-2.9.9/examples/testXPath.c
/usr/share/doc/libxml2-2.9.9/examples/xmllint.c
/usr/share/doc/libxml2-2.9.9/html/DOM.gif
/usr/share/doc/libxml2-2.9.9/html/FAQ.html
/usr/share/doc/libxml2-2.9.9/html/Libxml2-Logo-180x168.gif
/usr/share/doc/libxml2-2.9.9/html/Libxml2-Logo-90x34.gif
/usr/share/doc/libxml2-2.9.9/html/encoding.html
/usr/share/doc/libxml2-2.9.9/html/examples.xml
/usr/share/doc/libxml2-2.9.9/html/examples.xsl
/usr/share/doc/libxml2-2.9.9/html/html/book1.html
/usr/share/doc/libxml2-2.9.9/html/html/home.png
/usr/share/doc/libxml2-2.9.9/html/html/index.html
/usr/share/doc/libxml2-2.9.9/html/html/left.png
/usr/share/doc/libxml2-2.9.9/html/html/libxml-DOCBparser.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-HTMLparser.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-HTMLtree.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-SAX.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-SAX2.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-c14n.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-catalog.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-chvalid.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-debugXML.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-dict.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-encoding.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-entities.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-globals.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-hash.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-lib.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-list.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-nanoftp.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-nanohttp.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-parser.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-parserInternals.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-pattern.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-relaxng.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-schemasInternals.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-schematron.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-threads.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-tree.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-uri.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-valid.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xinclude.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xlink.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlIO.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlautomata.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlerror.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlexports.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlmemory.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlmodule.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlreader.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlregexp.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlsave.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlschemas.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlschemastypes.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlstring.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlunicode.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlversion.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xmlwriter.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xpath.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xpathInternals.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xpointer.html
/usr/share/doc/libxml2-2.9.9/html/html/libxml-xzlib.html
/usr/share/doc/libxml2-2.9.9/html/html/right.png
/usr/share/doc/libxml2-2.9.9/html/html/up.png
/usr/share/doc/libxml2-2.9.9/html/index.html
/usr/share/doc/libxml2-2.9.9/html/io1.c
/usr/share/doc/libxml2-2.9.9/html/io1.res
/usr/share/doc/libxml2-2.9.9/html/io2.c
/usr/share/doc/libxml2-2.9.9/html/io2.res
/usr/share/doc/libxml2-2.9.9/html/libxml.gif
/usr/share/doc/libxml2-2.9.9/html/parse1.c
/usr/share/doc/libxml2-2.9.9/html/parse2.c
/usr/share/doc/libxml2-2.9.9/html/parse3.c
/usr/share/doc/libxml2-2.9.9/html/parse4.c
/usr/share/doc/libxml2-2.9.9/html/reader1.c
/usr/share/doc/libxml2-2.9.9/html/reader1.res
/usr/share/doc/libxml2-2.9.9/html/reader2.c
/usr/share/doc/libxml2-2.9.9/html/reader3.c
/usr/share/doc/libxml2-2.9.9/html/reader3.res
/usr/share/doc/libxml2-2.9.9/html/reader4.c
/usr/share/doc/libxml2-2.9.9/html/reader4.res
/usr/share/doc/libxml2-2.9.9/html/redhat.gif
/usr/share/doc/libxml2-2.9.9/html/smallfootonly.gif
/usr/share/doc/libxml2-2.9.9/html/structure.gif
/usr/share/doc/libxml2-2.9.9/html/test1.xml
/usr/share/doc/libxml2-2.9.9/html/test2.xml
/usr/share/doc/libxml2-2.9.9/html/test3.xml
/usr/share/doc/libxml2-2.9.9/html/testWriter.c
/usr/share/doc/libxml2-2.9.9/html/tree1.c
/usr/share/doc/libxml2-2.9.9/html/tree1.res
/usr/share/doc/libxml2-2.9.9/html/tree2.c
/usr/share/doc/libxml2-2.9.9/html/tree2.res
/usr/share/doc/libxml2-2.9.9/html/tst.xml
/usr/share/doc/libxml2-2.9.9/html/tutorial/apa.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/apb.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/apc.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/apd.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ape.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/apf.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/apg.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/aph.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/api.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s02.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s03.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s04.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s05.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s06.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s07.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s08.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ar01s09.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/blank.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/1.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/10.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/2.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/3.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/4.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/5.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/6.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/7.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/8.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/callouts/9.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/caution.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/draft.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/home.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/important.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/next.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/note.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/prev.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/tip.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/toc-blank.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/toc-minus.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/toc-plus.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/up.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/images/warning.png
/usr/share/doc/libxml2-2.9.9/html/tutorial/includeaddattribute.c
/usr/share/doc/libxml2-2.9.9/html/tutorial/includeaddkeyword.c
/usr/share/doc/libxml2-2.9.9/html/tutorial/includeconvert.c
/usr/share/doc/libxml2-2.9.9/html/tutorial/includegetattribute.c
/usr/share/doc/libxml2-2.9.9/html/tutorial/includekeyword.c
/usr/share/doc/libxml2-2.9.9/html/tutorial/includexpath.c
/usr/share/doc/libxml2-2.9.9/html/tutorial/index.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/ix01.html
/usr/share/doc/libxml2-2.9.9/html/tutorial/xmltutorial.pdf
/usr/share/doc/libxml2-2.9.9/html/w3c.png
/usr/share/doc/libxml2-2.9.9/html/writer.xml
/usr/share/doc/libxml2-2.9.9/html/xml.html
/usr/share/doc/libxml2-2.9.9/html/xpath1.c
/usr/share/doc/libxml2-2.9.9/html/xpath1.res
/usr/share/doc/libxml2-2.9.9/html/xpath2.c
/usr/share/doc/libxml2-2.9.9/html/xpath2.res
/usr/share/doc/libxml2-python-2.9.9/TODO
/usr/share/doc/libxml2-python-2.9.9/examples/attribs.py
/usr/share/doc/libxml2-python-2.9.9/examples/build.py
/usr/share/doc/libxml2-python-2.9.9/examples/compareNodes.py
/usr/share/doc/libxml2-python-2.9.9/examples/ctxterror.py
/usr/share/doc/libxml2-python-2.9.9/examples/cutnpaste.py
/usr/share/doc/libxml2-python-2.9.9/examples/dtdvalid.py
/usr/share/doc/libxml2-python-2.9.9/examples/error.py
/usr/share/doc/libxml2-python-2.9.9/examples/inbuf.py
/usr/share/doc/libxml2-python-2.9.9/examples/indexes.py
/usr/share/doc/libxml2-python-2.9.9/examples/input_callback.py
/usr/share/doc/libxml2-python-2.9.9/examples/invalid.xml
/usr/share/doc/libxml2-python-2.9.9/examples/nsdel.py
/usr/share/doc/libxml2-python-2.9.9/examples/outbuf.py
/usr/share/doc/libxml2-python-2.9.9/examples/push.py
/usr/share/doc/libxml2-python-2.9.9/examples/pushSAX.py
/usr/share/doc/libxml2-python-2.9.9/examples/pushSAXhtml.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader2.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader3.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader4.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader5.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader6.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader7.py
/usr/share/doc/libxml2-python-2.9.9/examples/reader8.py
/usr/share/doc/libxml2-python-2.9.9/examples/readererr.py
/usr/share/doc/libxml2-python-2.9.9/examples/readernext.py
/usr/share/doc/libxml2-python-2.9.9/examples/regexp.py
/usr/share/doc/libxml2-python-2.9.9/examples/relaxng.py
/usr/share/doc/libxml2-python-2.9.9/examples/resolver.py
/usr/share/doc/libxml2-python-2.9.9/examples/schema.py
/usr/share/doc/libxml2-python-2.9.9/examples/serialize.py
/usr/share/doc/libxml2-python-2.9.9/examples/sync.py
/usr/share/doc/libxml2-python-2.9.9/examples/test.dtd
/usr/share/doc/libxml2-python-2.9.9/examples/thread2.py
/usr/share/doc/libxml2-python-2.9.9/examples/tst.py
/usr/share/doc/libxml2-python-2.9.9/examples/tst.xml
/usr/share/doc/libxml2-python-2.9.9/examples/tstLastError.py
/usr/share/doc/libxml2-python-2.9.9/examples/tstURI.py
/usr/share/doc/libxml2-python-2.9.9/examples/tstmem.py
/usr/share/doc/libxml2-python-2.9.9/examples/tstxpath.py
/usr/share/doc/libxml2-python-2.9.9/examples/valid.xml
/usr/share/doc/libxml2-python-2.9.9/examples/validDTD.py
/usr/share/doc/libxml2-python-2.9.9/examples/validRNG.py
/usr/share/doc/libxml2-python-2.9.9/examples/validSchemas.py
/usr/share/doc/libxml2-python-2.9.9/examples/validate.py
/usr/share/doc/libxml2-python-2.9.9/examples/walker.py
/usr/share/doc/libxml2-python-2.9.9/examples/xpath.py
/usr/share/doc/libxml2-python-2.9.9/examples/xpathext.py
/usr/share/doc/libxml2-python-2.9.9/examples/xpathleak.py
/usr/share/doc/libxml2-python-2.9.9/examples/xpathns.py
/usr/share/doc/libxml2-python-2.9.9/examples/xpathret.py
/usr/share/gtk-doc/html/libxml2/general.html
/usr/share/gtk-doc/html/libxml2/home.png
/usr/share/gtk-doc/html/libxml2/index.html
/usr/share/gtk-doc/html/libxml2/left.png
/usr/share/gtk-doc/html/libxml2/libxml2-DOCBparser.html
/usr/share/gtk-doc/html/libxml2/libxml2-HTMLparser.html
/usr/share/gtk-doc/html/libxml2/libxml2-HTMLtree.html
/usr/share/gtk-doc/html/libxml2/libxml2-SAX.html
/usr/share/gtk-doc/html/libxml2/libxml2-SAX2.html
/usr/share/gtk-doc/html/libxml2/libxml2-c14n.html
/usr/share/gtk-doc/html/libxml2/libxml2-catalog.html
/usr/share/gtk-doc/html/libxml2/libxml2-chvalid.html
/usr/share/gtk-doc/html/libxml2/libxml2-debugXML.html
/usr/share/gtk-doc/html/libxml2/libxml2-dict.html
/usr/share/gtk-doc/html/libxml2/libxml2-encoding.html
/usr/share/gtk-doc/html/libxml2/libxml2-entities.html
/usr/share/gtk-doc/html/libxml2/libxml2-globals.html
/usr/share/gtk-doc/html/libxml2/libxml2-hash.html
/usr/share/gtk-doc/html/libxml2/libxml2-list.html
/usr/share/gtk-doc/html/libxml2/libxml2-nanoftp.html
/usr/share/gtk-doc/html/libxml2/libxml2-nanohttp.html
/usr/share/gtk-doc/html/libxml2/libxml2-parser.html
/usr/share/gtk-doc/html/libxml2/libxml2-parserInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-pattern.html
/usr/share/gtk-doc/html/libxml2/libxml2-relaxng.html
/usr/share/gtk-doc/html/libxml2/libxml2-schemasInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-schematron.html
/usr/share/gtk-doc/html/libxml2/libxml2-threads.html
/usr/share/gtk-doc/html/libxml2/libxml2-tree.html
/usr/share/gtk-doc/html/libxml2/libxml2-uri.html
/usr/share/gtk-doc/html/libxml2/libxml2-valid.html
/usr/share/gtk-doc/html/libxml2/libxml2-xinclude.html
/usr/share/gtk-doc/html/libxml2/libxml2-xlink.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlIO.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlautomata.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlerror.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlexports.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlmemory.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlmodule.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlreader.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlregexp.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlsave.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlschemas.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlschemastypes.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlstring.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlunicode.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlversion.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlwriter.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpath.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpathInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpointer.html
/usr/share/gtk-doc/html/libxml2/libxml2.devhelp
/usr/share/gtk-doc/html/libxml2/right.png
/usr/share/gtk-doc/html/libxml2/style.css
/usr/share/gtk-doc/html/libxml2/up.png
/usr/share/man/man1/xml2-config.1.gz
/usr/share/man/man1/xmlcatalog.1.gz
/usr/share/man/man1/xmllint.1.gz
/usr/share/man/man3/libxml.3.gz

%changelog
# let's skip this for now

