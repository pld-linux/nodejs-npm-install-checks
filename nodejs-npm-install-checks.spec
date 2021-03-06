%define		pkg	npm-install-checks
Summary:	Checks that npm runs during the installation of a module
Name:		nodejs-%{pkg}
Version:	1.0.5
Release:	1
License:	BSD-2-Clause
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	72997d88cf249ba2ab284eb3045841c5
URL:		https://github.com/robertkowalski/npm-install-checks
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-npmlog < 2.0.0
Requires:	nodejs-npmlog >= 0.1.0
Requires:	nodejs-semver < 5.0.0
Requires:	nodejs-semver >= 2.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks that npm runs during the installation of a module.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
