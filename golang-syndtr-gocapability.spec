%define prerelease 3454319be2ebde8481aa0804a801f4d07de705b5
%define import_path github.com/syndtr/gocapability
%define gosrc %{go_dir}/src/pkg/%{import_path}
%define shortcommit %(c=%{prerelease}; echo ${c:0:7})
%define	debug_package %nil

Summary:	Utilities for manipulating POSIX capabilities in Go
Name:		golang-syndtr-gocapability
Version:	0.1.git%{shortcommit}
Release:	2
License:	MIT
Group:		Development/Other
Url:		https://%{import_path}
Source0:        https://%{import_path}/archive/%{prerelease}.tar.gz
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path}/capability) = %{version}-%{release}
BuildRequires:	golang

%description
Utilities for manipulating POSIX capabilities in Go

%prep
%setup -q -n gocapability-%{prerelease}

%build

%install
mkdir -p %{buildroot}%{gosrc}
cp -av * %{buildroot}%{gosrc}/
rm -f %{buildroot}%{gosrc}/LICENSE

%files
%doc LICENSE
%{gosrc}/*
