Summary:	A program for easy modifying file /etc/fstab
Summary(pl):	Program do �atwej modyfikacji pliku /etc/fstab
Name:		kfstab
Version:	0.7.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Vendor:		Andreas Reuter <Andreas.Reuter@andreas-reuter.de>
Source0:	http://dl.sourceforge.net/kfstab/%{name}-%{version}.tgz
# Source0-md5:	558ecd04b0924df30fd822192422e030
Patch0:		%{name}-morefilesystems.patch
Patch1:		%{name}-desktopfile.patch
URL:		http://kfstab.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0.0
Requires:	kdelibs >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A program for easy modifying /etc/fstab .

%description -l pl
Program do �atwej modyfikacji pliku /etc/fstab .

%prep
%setup -q -n %{name} 
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_kdedocdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/applnk/System/%{name}.desktop \
   $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
mv $RPM_BUILD_ROOT%{_docdir}/HTML/en \
   $RPM_BUILD_ROOT%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*
