# revision 24694
# category Package
# catalog-ctan /macros/latex/contrib/magaz
# catalog-date 2011-11-29 11:02:24 +0100
# catalog-license other-free
# catalog-version 0.4
Name:		texlive-magaz
Version:	0.4
Release:	3
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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/magaz/magaz.sty
%doc %{_texmfdistdir}/doc/latex/magaz/magaz.pdf
%doc %{_texmfdistdir}/doc/latex/magaz/magaz.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 753676
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 739825
- texlive-magaz

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718938
- texlive-magaz
- texlive-magaz
- texlive-magaz
- texlive-magaz

