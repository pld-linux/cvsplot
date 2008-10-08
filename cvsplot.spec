Summary:	Cvsplot is used for collecting statistics from CVS
Summary(pl.UTF-8):	Cvsplot pokazuje statystyki z CVS
Name:		cvsplot
Version:	1.7.4
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/cvsplot/%{name}-%{version}.tar.gz
# Source0-md5:	50315fad42d7ca5f94ccdd4f5d25ee03
URL:		http://cvsplot.sourceforge.net/
Requires:	perl-Date-Manip
Requires:	perl-String-ShellQuote
Suggests:	gnuplot
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cvsplot is used for collecting statistics from CVS controlled files.
Simple statistics such as how the total number of files and lines of
code change against time. It runs under any flavour of UNIX, and under
Windows (assuming Perl from http://www.activestate.com/ is installed).

%description -l pl.UTF-8
Cvsplot to narzędzie do prezentowania statystyk z repozytoriów CVS.
Przykładowo jak zmieniała się sumaryczna liczba plików w zadanym
przedziale czasowym. Działa na każdym Uniksie, a także w Windows (przy
założeniu, że zostanie zainstalowana wersja Perla z
http://www.activestate.com/).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name}.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.pl
%doc CHANGELOG README LICENSE
