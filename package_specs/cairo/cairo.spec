Name:       cairo
Version:    1.16.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -a 0

%build
%configure  --disable-static --enable-tee
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/cairo-sphinx
/usr/bin/cairo-trace
/usr/include/cairo/cairo-deprecated.h
/usr/include/cairo/cairo-features.h
/usr/include/cairo/cairo-ft.h
/usr/include/cairo/cairo-gobject.h
/usr/include/cairo/cairo-pdf.h
/usr/include/cairo/cairo-ps.h
/usr/include/cairo/cairo-script-interpreter.h
/usr/include/cairo/cairo-script.h
/usr/include/cairo/cairo-svg.h
/usr/include/cairo/cairo-tee.h
/usr/include/cairo/cairo-version.h
/usr/include/cairo/cairo-xcb.h
/usr/include/cairo/cairo-xlib-xrender.h
/usr/include/cairo/cairo-xlib.h
/usr/include/cairo/cairo.h
/usr/lib64/cairo/cairo-fdr.la
/usr/lib64/cairo/cairo-fdr.so
/usr/lib64/cairo/cairo-sphinx.la
/usr/lib64/cairo/cairo-sphinx.so
/usr/lib64/cairo/libcairo-trace.la
/usr/lib64/cairo/libcairo-trace.so
/usr/lib64/libcairo-gobject.la
/usr/lib64/libcairo-gobject.so
/usr/lib64/libcairo-gobject.so.2
/usr/lib64/libcairo-gobject.so.2.11600.0
/usr/lib64/libcairo-script-interpreter.la
/usr/lib64/libcairo-script-interpreter.so
/usr/lib64/libcairo-script-interpreter.so.2
/usr/lib64/libcairo-script-interpreter.so.2.11600.0
/usr/lib64/libcairo.la
/usr/lib64/libcairo.so
/usr/lib64/libcairo.so.2
/usr/lib64/libcairo.so.2.11600.0
/usr/lib64/pkgconfig/cairo-fc.pc
/usr/lib64/pkgconfig/cairo-ft.pc
/usr/lib64/pkgconfig/cairo-gobject.pc
/usr/lib64/pkgconfig/cairo-pdf.pc
/usr/lib64/pkgconfig/cairo-png.pc
/usr/lib64/pkgconfig/cairo-ps.pc
/usr/lib64/pkgconfig/cairo-script.pc
/usr/lib64/pkgconfig/cairo-svg.pc
/usr/lib64/pkgconfig/cairo-tee.pc
/usr/lib64/pkgconfig/cairo-xcb-shm.pc
/usr/lib64/pkgconfig/cairo-xcb.pc
/usr/lib64/pkgconfig/cairo-xlib-xrender.pc
/usr/lib64/pkgconfig/cairo-xlib.pc
/usr/lib64/pkgconfig/cairo.pc
/usr/share/gtk-doc/html/cairo/bindings-errors.html
/usr/share/gtk-doc/html/cairo/bindings-fonts.html
/usr/share/gtk-doc/html/cairo/bindings-memory.html
/usr/share/gtk-doc/html/cairo/bindings-overloading.html
/usr/share/gtk-doc/html/cairo/bindings-path.html
/usr/share/gtk-doc/html/cairo/bindings-patterns.html
/usr/share/gtk-doc/html/cairo/bindings-return-values.html
/usr/share/gtk-doc/html/cairo/bindings-streams.html
/usr/share/gtk-doc/html/cairo/bindings-surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Error-handling.html
/usr/share/gtk-doc/html/cairo/cairo-FreeType-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Image-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-PDF-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-PNG-Support.html
/usr/share/gtk-doc/html/cairo/cairo-Paths.html
/usr/share/gtk-doc/html/cairo/cairo-PostScript-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Quartz-(CGFont)-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Quartz-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Raster-Sources.html
/usr/share/gtk-doc/html/cairo/cairo-Recording-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Regions.html
/usr/share/gtk-doc/html/cairo/cairo-SVG-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Script-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Tags-and-Links.html
/usr/share/gtk-doc/html/cairo/cairo-Transformations.html
/usr/share/gtk-doc/html/cairo/cairo-Types.html
/usr/share/gtk-doc/html/cairo/cairo-User-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Version-Information.html
/usr/share/gtk-doc/html/cairo/cairo-Win32-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Win32-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XCB-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XLib-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XLib-XRender-Backend.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-device-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-font-face-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-font-options-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-matrix-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-pattern-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-scaled-font-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-surface-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-t.html
/usr/share/gtk-doc/html/cairo/cairo-drawing.html
/usr/share/gtk-doc/html/cairo/cairo-fonts.html
/usr/share/gtk-doc/html/cairo/cairo-support.html
/usr/share/gtk-doc/html/cairo/cairo-surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-text.html
/usr/share/gtk-doc/html/cairo/cairo.devhelp2
/usr/share/gtk-doc/html/cairo/home.png
/usr/share/gtk-doc/html/cairo/index-1.10.html
/usr/share/gtk-doc/html/cairo/index-1.12.html
/usr/share/gtk-doc/html/cairo/index-1.14.html
/usr/share/gtk-doc/html/cairo/index-1.16.html
/usr/share/gtk-doc/html/cairo/index-1.2.html
/usr/share/gtk-doc/html/cairo/index-1.4.html
/usr/share/gtk-doc/html/cairo/index-1.6.html
/usr/share/gtk-doc/html/cairo/index-1.8.html
/usr/share/gtk-doc/html/cairo/index-all.html
/usr/share/gtk-doc/html/cairo/index.html
/usr/share/gtk-doc/html/cairo/language-bindings.html
/usr/share/gtk-doc/html/cairo/left-insensitive.png
/usr/share/gtk-doc/html/cairo/left.png
/usr/share/gtk-doc/html/cairo/right-insensitive.png
/usr/share/gtk-doc/html/cairo/right.png
/usr/share/gtk-doc/html/cairo/style.css
/usr/share/gtk-doc/html/cairo/up-insensitive.png
/usr/share/gtk-doc/html/cairo/up.png

%changelog
# let's skip this for now

