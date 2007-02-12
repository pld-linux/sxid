Summary:	suid, sgid file and directory checking
Summary(pl.UTF-8):   Narzędzie sprawdzające pliki i katalogi o atrybutach suid i sgid
Name:		sxid
Version:	4.0.2
Release:	4
License:	GPL
Group:		Applications/System
Source0:	ftp://marcus.seva.net/pub/sxid/%{name}_%{version}.tar.gz
# Source0-md5:	feedb01a5e93f8ba9f38a8054f3ef04b
BuildRequires:	autoconf
Requires:	crondaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/%{name}

%description
This program runs as a cronjob. Basically it tracks any changes in
your s[ug]id files and folders. If there are any new ones, ones that
aren't set any more, or they have changed bits or other modes then it
reports the changes. You can also run this manually for spot checking.

It tracks s[ug]id files by md5 checksums. This helps detect if your
files have been tampered with, would not show under normal name and
permissions checking. Directories are tracked by inodes.

%description -l pl.UTF-8
Ten program jest uruchamiany z crona. Śledzi on zmiany w plikach i
katalogach o atrybutach s[ug]id. Jeżeli pojawiają sie nowe, takie
których jeszcze nie zna lub takie, które sie zmieniły wtedy raportuje
zmiany. Można go także uruchamiać ręcznie do natychmiastowego
sprawdzenia.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT/etc/cron.daily
install debian/cron.daily $RPM_BUILD_ROOT/etc/cron.daily/sxid

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/sxid.conf.example
%attr(755,root,root) %{_bindir}/*
%attr(700,root,root) /etc/cron.daily/sxid
%{_mandir}/man?/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
