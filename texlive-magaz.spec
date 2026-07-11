%global tl_name magaz
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Magazine layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/magaz
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/magaz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/magaz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The current version does special formatting for the first line of text
in a paragraph. The package is part of a larger body of tools which
remain in preparation.

