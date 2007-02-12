Summary:	PAM module for Ruby
Summary(pl.UTF-8):   Moduł PAM dla języka Ruby
Name:		ruby-PAM
Version:	1.5.2
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-pam/ruby-pam-%{version}.tar.gz
# Source0-md5:	bf61416ddc429600812b7452f16b1c7b
URL:		http://ruby-pam.sourceforge.net/ruby-pam.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	pam-devel
BuildRequires:	ruby-devel
Obsoletes:	ruby-pam
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/PAM (aka ruby-pam) is an extension library which provides the
interface to PAM APIs.

%description -l pl.UTF-8
Ruby/PAM (zwany też ruby-pam) to biblioteka rozszerzająca język Ruby
udostępniająca interfejs do API PAM.

%prep
%setup -q -n ruby-pam-%{version}

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitearchdir}

install pam.so $RPM_BUILD_ROOT%{ruby_sitearchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{ruby_sitearchdir}/*.so
