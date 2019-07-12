Name:       libarchive
Version:    3.4.0
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
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/bsdcat
/usr/bin/bsdcpio
/usr/bin/bsdtar
/usr/include/archive.h
/usr/include/archive_entry.h
/usr/lib64/libarchive.a
/usr/lib64/libarchive.la
/usr/lib64/libarchive.so
/usr/lib64/libarchive.so.13
/usr/lib64/libarchive.so.13.4.0
/usr/lib64/pkgconfig/libarchive.pc
/usr/share/man/man1/bsdcat.1.gz
/usr/share/man/man1/bsdcpio.1.gz
/usr/share/man/man1/bsdtar.1.gz
/usr/share/man/man3/archive_entry.3.gz
/usr/share/man/man3/archive_entry_acl.3.gz
/usr/share/man/man3/archive_entry_linkify.3.gz
/usr/share/man/man3/archive_entry_misc.3.gz
/usr/share/man/man3/archive_entry_paths.3.gz
/usr/share/man/man3/archive_entry_perms.3.gz
/usr/share/man/man3/archive_entry_stat.3.gz
/usr/share/man/man3/archive_entry_time.3.gz
/usr/share/man/man3/archive_read.3.gz
/usr/share/man/man3/archive_read_add_passphrase.3.gz
/usr/share/man/man3/archive_read_data.3.gz
/usr/share/man/man3/archive_read_disk.3.gz
/usr/share/man/man3/archive_read_extract.3.gz
/usr/share/man/man3/archive_read_filter.3.gz
/usr/share/man/man3/archive_read_format.3.gz
/usr/share/man/man3/archive_read_free.3.gz
/usr/share/man/man3/archive_read_header.3.gz
/usr/share/man/man3/archive_read_new.3.gz
/usr/share/man/man3/archive_read_open.3.gz
/usr/share/man/man3/archive_read_set_options.3.gz
/usr/share/man/man3/archive_util.3.gz
/usr/share/man/man3/archive_write.3.gz
/usr/share/man/man3/archive_write_blocksize.3.gz
/usr/share/man/man3/archive_write_data.3.gz
/usr/share/man/man3/archive_write_disk.3.gz
/usr/share/man/man3/archive_write_filter.3.gz
/usr/share/man/man3/archive_write_finish_entry.3.gz
/usr/share/man/man3/archive_write_format.3.gz
/usr/share/man/man3/archive_write_free.3.gz
/usr/share/man/man3/archive_write_header.3.gz
/usr/share/man/man3/archive_write_new.3.gz
/usr/share/man/man3/archive_write_open.3.gz
/usr/share/man/man3/archive_write_set_options.3.gz
/usr/share/man/man3/archive_write_set_passphrase.3.gz
/usr/share/man/man3/libarchive.3.gz
/usr/share/man/man3/libarchive_changes.3.gz
/usr/share/man/man3/libarchive_internals.3.gz
/usr/share/man/man5/cpio.5.gz
/usr/share/man/man5/libarchive-formats.5.gz
/usr/share/man/man5/mtree.5.gz
/usr/share/man/man5/tar.5.gz

%changelog
# let's skip this for now
