Name:       gdbm
Version:    1.18.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --disable-static \
           --enable-libgdbm-compat
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool
/usr/include/dbm.h
/usr/include/gdbm.h
/usr/include/ndbm.h
/usr/lib64/libgdbm.la
/usr/lib64/libgdbm.so
/usr/lib64/libgdbm.so.6
/usr/lib64/libgdbm.so.6.0.0
/usr/lib64/libgdbm_compat.la
/usr/lib64/libgdbm_compat.so
/usr/lib64/libgdbm_compat.so.4
/usr/lib64/libgdbm_compat.so.4.0.0
/usr/share/info/gdbm.info.gz
/usr/share/locale/da/LC_MESSAGES/gdbm.mo
/usr/share/locale/de/LC_MESSAGES/gdbm.mo
/usr/share/locale/eo/LC_MESSAGES/gdbm.mo
/usr/share/locale/es/LC_MESSAGES/gdbm.mo
/usr/share/locale/fi/LC_MESSAGES/gdbm.mo
/usr/share/locale/fr/LC_MESSAGES/gdbm.mo
/usr/share/locale/ja/LC_MESSAGES/gdbm.mo
/usr/share/locale/pl/LC_MESSAGES/gdbm.mo
/usr/share/locale/pt_BR/LC_MESSAGES/gdbm.mo
/usr/share/locale/sr/LC_MESSAGES/gdbm.mo
/usr/share/locale/sv/LC_MESSAGES/gdbm.mo
/usr/share/locale/uk/LC_MESSAGES/gdbm.mo
/usr/share/locale/vi/LC_MESSAGES/gdbm.mo
/usr/share/man/man1/gdbm_dump.1.gz
/usr/share/man/man1/gdbm_load.1.gz
/usr/share/man/man1/gdbmtool.1.gz
/usr/share/man/man3/gdbm.3.gz

%changelog
# let's skip this for now
