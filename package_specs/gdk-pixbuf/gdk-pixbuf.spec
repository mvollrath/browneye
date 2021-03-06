Name:       gdk-pixbuf
Version:    2.38.0
Release:    3
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(gdk-pixbuf-2.0)
Requires: librsvg

%description
TODO

%prep
%setup -a 0

%build
mkdir build-pb
pushd build-pb

meson --prefix=/usr -Dman=false ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-pb
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%post
gdk-pixbuf-query-loaders > /usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders.cache
gdk-pixbuf-query-loaders --update-cache

%files
/usr/bin/gdk-pixbuf-csource
/usr/bin/gdk-pixbuf-pixdata
/usr/bin/gdk-pixbuf-query-loaders
/usr/bin/gdk-pixbuf-thumbnailer
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-animation.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-autocleanups.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-core.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-enum-types.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-features.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-io.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-loader.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-macros.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-marshal.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-simple-anim.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-transform.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixdata.h
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-bmp.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-gif.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ico.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-jpeg.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-png.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.so
/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.so
/usr/lib/girepository-1.0/GdkPixbuf-2.0.typelib
/usr/lib/girepository-1.0/GdkPixdata-2.0.typelib
/usr/lib/libgdk_pixbuf-2.0.so
/usr/lib/libgdk_pixbuf-2.0.so.0
/usr/lib/libgdk_pixbuf-2.0.so.0.3800.0
/usr/lib/libgdk_pixbuf_xlib-2.0.so
/usr/lib/libgdk_pixbuf_xlib-2.0.so.0
/usr/lib/libgdk_pixbuf_xlib-2.0.so.0.3800.0
/usr/lib/pkgconfig/gdk-pixbuf-2.0.pc
/usr/lib/pkgconfig/gdk-pixbuf-xlib-2.0.pc
/usr/libexec/installed-tests/gdk-pixbuf/1_partyanimsm2.gif
/usr/libexec/installed-tests/gdk-pixbuf/aero.gif
/usr/libexec/installed-tests/gdk-pixbuf/animation
/usr/libexec/installed-tests/gdk-pixbuf/bug143608-comment.jpg
/usr/libexec/installed-tests/gdk-pixbuf/bug725582-testrotate.jpg
/usr/libexec/installed-tests/gdk-pixbuf/bug725582-testrotate.png
/usr/libexec/installed-tests/gdk-pixbuf/bug753605-atsize.jpg
/usr/libexec/installed-tests/gdk-pixbuf/bug775218.jpg
/usr/libexec/installed-tests/gdk-pixbuf/bug775229.pixdata
/usr/libexec/installed-tests/gdk-pixbuf/bug775693.pixdata
/usr/libexec/installed-tests/gdk-pixbuf/cve-2015-4491
/usr/libexec/installed-tests/gdk-pixbuf/cve-2015-4491.bmp
/usr/libexec/installed-tests/gdk-pixbuf/dpi.jpeg
/usr/libexec/installed-tests/gdk-pixbuf/dpi.png
/usr/libexec/installed-tests/gdk-pixbuf/dpi.tiff
/usr/libexec/installed-tests/gdk-pixbuf/icc-profile.jpeg
/usr/libexec/installed-tests/gdk-pixbuf/icc-profile.png
/usr/libexec/installed-tests/gdk-pixbuf/large.jpg
/usr/libexec/installed-tests/gdk-pixbuf/large.png
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-area-updated
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-composite
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-dpi
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-fail
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-icc
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-icon-serialize
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-jpeg
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-pixdata
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-randomly-modified
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-readonly-to-mutable
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-reftest
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-resource
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-save
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-scale
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-scale-two-step
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-short-gif-write
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-stream
/usr/libexec/installed-tests/gdk-pixbuf/pixbuf-threads
/usr/libexec/installed-tests/gdk-pixbuf/premature-end.jpg
/usr/libexec/installed-tests/gdk-pixbuf/premature-end.png
/usr/libexec/installed-tests/gdk-pixbuf/test-animation.ani
/usr/libexec/installed-tests/gdk-pixbuf/test-animation.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-image-rle.pixdata
/usr/libexec/installed-tests/gdk-pixbuf/test-image.pixdata
/usr/libexec/installed-tests/gdk-pixbuf/test-image.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/CVE-2017-2862.jpg
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/DoS.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/androstanRezeptor.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug776694.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug777315.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug778204.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug778584.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug779012.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug779016-infinite.icns
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug780269.tif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug784903-overflow-dimensions.tiff
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/bug785973.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/colormap-image-without-colormap.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/empty-file.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/file3.jp2
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.1.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.1.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.1.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.1.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.1.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.2.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.2.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.2.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.3.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.3.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.3.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.3.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.4.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.4.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.5.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.6.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.7.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/invalid.8.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/fail/overflow.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/bad-header.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/bmp-line-overflow.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/bug775232.pnm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/bug775242.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/bug775648.qtif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/bug775697.jpg
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/bug776040.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/crash.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/decodecolormap.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/invalid.1.xpm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/invalid.2.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/invalid.4.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.gif
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.jp2
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.jpeg
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.tiff
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.xbm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.1.xpm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.2.jpeg
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.2.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.2.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.3.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/randomly-modified/valid.4.ppm
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/bug696331.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/bug696331.png.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/bug785447.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/bug785447.ico.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/cat.jpg
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/cat.jpg.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/colormap-too-small.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/colormap-too-small.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/mandatory-bitmasks.bmp
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/mandatory-bitmasks.bmp.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/rle-too-many-pixels-2.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/rle-too-many-pixels-2.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/rle-too-many-pixels.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/rle-too-many-pixels.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/squares.ico
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/squares.ico.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-16bpp.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-24bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-32bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-8bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap-rle-8bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-cmap.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-16bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-8bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-opaque.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-16bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray-rle-8bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-gray.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-opaque.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-24bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-bottom-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-bottom-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-bottom-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-bottom-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-top-left.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-top-left.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-top-right.tga
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo-rle-32bpp-top-right.tga.ref.png
/usr/libexec/installed-tests/gdk-pixbuf/test-images/reftests/tga/gtk-logo.ref.png
/usr/share/gir-1.0/GdkPixbuf-2.0.gir
/usr/share/gir-1.0/GdkPixdata-2.0.gir
/usr/share/installed-tests/gdk-pixbuf/animation.test
/usr/share/installed-tests/gdk-pixbuf/cve-2015-4491.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-area-updated.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-composite.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-dpi.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-fail.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-icc.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-icon-serialize.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-jpeg.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-pixdata.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-randomly-modified.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-readonly-to-mutable.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-reftest.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-resource.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-save.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-scale-two-step.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-scale.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-short-gif-write.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-stream.test
/usr/share/installed-tests/gdk-pixbuf/pixbuf-threads.test
/usr/share/locale/af/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ang/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ar/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/as/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ast/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/az/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/be/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/be@latin/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/bg/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/bn/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/bn_IN/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/br/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/bs/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ca/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ca@valencia/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/crh/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/cs/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/csb/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/cy/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/da/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/de/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/dz/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/el/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/en@shaw/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/en_CA/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/en_GB/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/eo/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/es/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/et/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/eu/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/fa/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/fi/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/fr/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/fur/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ga/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/gl/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/gu/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/he/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/hi/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/hr/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/hu/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/hy/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ia/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/id/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/io/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/is/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/it/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ja/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ka/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/kk/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/km/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/kn/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ko/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ku/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/li/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/lt/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/lv/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/mai/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/mi/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/mk/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ml/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/mn/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/mr/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ms/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/my/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/nb/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/nds/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ne/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/nl/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/nn/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/nso/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/oc/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/or/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/pa/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/pl/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ps/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/pt/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/pt_BR/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ro/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ru/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/si/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/sk/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/sl/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/sq/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/sr/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/sr@ije/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/sr@latin/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/sv/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ta/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/te/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/tg/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/th/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/tk/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/tr/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/tt/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/ug/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/uk/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/uz/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/uz@cyrillic/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/vi/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/wa/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/xh/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/yi/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/zh_CN/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/zh_HK/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/locale/zh_TW/LC_MESSAGES/gdk-pixbuf.mo
/usr/share/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer

%changelog
# let's skip this for now

