# revision 17431
# category Package
# catalog-ctan /macros/latex/contrib/magaz
# catalog-date 2010-03-17 12:20:59 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-magaz
Version:	0.2
Release:	1
Summary:	Magazine layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/magaz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magaz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magaz.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The current version does special formatting for the first line
of text in a paragraph. The package is part of a larger body of
tools which remain in preparation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
