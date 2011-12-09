# revision 24694
# category Package
# catalog-ctan /macros/latex/contrib/magaz
# catalog-date 2011-11-29 11:02:24 +0100
# catalog-license other-free
# catalog-version 0.4
Name:		texlive-magaz
Version:	0.4
Release:	1
Summary:	Magazine layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/magaz
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magaz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magaz.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The current version does special formatting for the first line
of text in a paragraph. The package is part of a larger body of
tools which remain in preparation.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/magaz/magaz.sty
%doc %{_texmfdistdir}/doc/latex/magaz/magaz.pdf
%doc %{_texmfdistdir}/doc/latex/magaz/magaz.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
