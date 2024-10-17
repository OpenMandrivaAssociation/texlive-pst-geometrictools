Name:		texlive-pst-geometrictools
Version:	70953
Release:	1
Summary:	A PSTricks package to draw geometric tools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-geometrictools
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-geometrictools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-geometrictools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This PSTricks package facilitates the drawing of protractors,
rulers, compasses and pencils.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-geometrictools
%{_texmfdistdir}/tex/generic/pst-geometrictools
%doc %{_texmfdistdir}/doc/generic/pst-geometrictools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
