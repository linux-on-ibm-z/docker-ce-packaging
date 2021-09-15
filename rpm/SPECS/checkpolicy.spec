Name:           checkpolicy
Version:        3.2.61.1
Release:        1%{?dist}
Group:          System Environment/Base
Summary:        policycoreutils package
License:        GPLv2
%description

BuildRequires: wget
BuildRequires: tar
BuildRequires: gcc7
BuildRequires: make
BuildRequires: gzip
BuildRequires: bison
BuildRequires: libsepol-devel
BuildRequires: flex

%configure

%install
wget https://github.com/SELinuxProject/selinux/releases/download/3.2/libsepol-3.2.tar.gz
tar -xvf libsepol-3.2.tar.gz
cd libsepol-3.2
make CC=gcc
cd ..
wget https://github.com/SELinuxProject/selinux/releases/download/3.2/checkpolicy-3.2.tar.gz
tar -xvf checkpolicy-3.2.tar.gz
cd checkpolicy-3.2
make CC=gcc
%files
