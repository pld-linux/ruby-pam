%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')
Summary:	PAM module for Ruby
Summary(pl):	Modu³ PAM dla jêzyka Ruby
Name:		ruby-pam
Version:	1.5.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-pam/%{name}-%{version}.tar.gz
# Source0-md5:	a6437f94621811cda255c69d6bb3a673
URL:		http://ruby-pam.sourceforge.net/ruby-pam.html
BuildRequires:	pam-devel
BuildRequires:	ruby-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/PAM (aka ruby-pam) is an extension library which provides the
interface to PAM APIs.

%description -l pl
Ruby/PAM (zwany te¿ ruby-pam) to biblioteka rozszerzaj±ca jêzyk Ruby
udostêpniaj±ca interfejs do API PAM.

%prep
%setup -q 

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
%doc ChangeLog README README.html
%attr(755,root,root) %{ruby_sitearchdir}/*.so
