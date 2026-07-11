%global tl_name francais-bst
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0a
Release:	%{tl_revision}.1
Summary:	Bibliographies conforming to French typographic standards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/francais-bst
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/francais-bst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/francais-bst.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/francais-bst.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides bibliographies (in French) conforming to the rules
in "Guide de la communication ecrite" (Malo, M., Quebec Amerique, 1996.
ISBN 978-2-8903-7875-9). The BibTeX styles were generated using custom-
bib and they are compatible with natbib.

