%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')
Summary:	PAM module for Ruby
Name:		ruby-pam
Version:	1.5.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-pam/%{name}-%{version}.tar.gz
# Source0-md5:	a6437f94621811cda255c69d6bb3a673
URL:		http://ruby-pam.sourceforge.net/ruby-pam.html
BuildRequires:	pam-devel
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module for Ruby

#%package devel
#Summary: Headers for the Ruby-pam module
#Group:	Development/Libraries

#%description devel
#Headers for the Ruby-pam module

%prep
%setup -q 

%build
# not autoconf-generated
ruby extconf.rb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitearchdir}
#install -d $RPM_BUILD_ROOT%{_includedir}/ruby-pam

install pam.so $RPM_BUILD_ROOT%{ruby_sitearchdir}
#install pam.h $RPM_BUILD_ROOT%{_includedir}/ruby-pam/
#install extconf.rb $RPM_BUILD_ROOT%{_includedir}/ruby-pam/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.html
%attr(755,root,root) %{ruby_sitearchdir}/*.so

#%files devel
#%defattr(644,root,root,755)
#%{_includedir}/ruby-pam
