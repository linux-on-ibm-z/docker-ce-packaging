Name:           policycoreutils
Version:        3.2
Release:        1%{?dist}
Group:          System Environment/Base
Summary:        policycoreutils package
License:        GPLv2
%description

%configure

BuildRequires: gzip
BuildRequires: make
BuildRequires: gcc7
BuildRequires: flex
BuildRequires: libbz2-devel
BuildRequires: libsemanage-devel
BuildRequires: gettext
BuildRequires: bison
BuildRequires: wget
BuildRequires: tar

%install
wget https://github.com/SELinuxProject/selinux/releases/download/3.2/libsepol-3.2.tar.gz
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 7
tar -xvf libsepol-3.2.tar.gz
cd libsepol-3.2
make CC=gcc
make install
cd ..
wget https://github.com/SELinuxProject/selinux/releases/download/3.2/libselinux-3.2.tar.gz
tar -xvf libselinux-3.2.tar.gz
cd libselinux-3.2
make CC=gcc
make install
cd ..
wget https://github.com/SELinuxProject/selinux/releases/download/3.2/policycoreutils-3.2.tar.gz
tar -xvf policycoreutils-3.2.tar.gz
cd policycoreutils-3.2
make CC=gcc
make install
%files
