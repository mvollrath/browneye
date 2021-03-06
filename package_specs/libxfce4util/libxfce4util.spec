Name:       libxfce4util
Version:    4.14.0
Release:    1
Summary:    Basic utility library for Xfce4.
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Basic utility library for Xfce4.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/xfce4/libxfce4util/*
/usr/lib64/girepository-1.0/libxfce4util-1.0.typelib
/usr/lib64/libxfce4util.la
/usr/lib64/libxfce4util.so
/usr/lib64/libxfce4util.so.7
/usr/lib64/libxfce4util.so.7.0.0
/usr/lib64/pkgconfig/libxfce4util-1.0.pc
/usr/sbin/xfce4-kiosk-query
/usr/share/gir-1.0/libxfce4util-1.0.gir
/usr/share/gtk-doc/html/libxfce4util/*
/usr/share/locale/*
/usr/share/vala/vapi/libxfce4util-1.0.vapi

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

