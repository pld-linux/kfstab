Summary:	A program for easy modyfing file /etc/fstab
Summary(pl):	Program do ³atwej modyfikacji pliku /etc/fstab
Name:		kfstab
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Andreas Reuter <Andreas.Reuter@andreas-reuter.de>
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	558ecd04b0924df30fd822192422e030
Patch:		%{name}-morefilesystems.patch
URL:		http://kfstab.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.0.0
Requires:	kdelibs >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define	_prefix	/usr/X11R6

%description
A program for easy modyfing /etc/fstab.
%description -l pl
Program do modyfikacji pliku /etc/fstab
%prep
%setup -q -n %{name} 
%patch -p1
%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applnk/*
%{_datadir}/apps/*
%{_datadir}/icons/*
#{_datadir}/locale/*	# nothing there
