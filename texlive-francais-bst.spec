Name:		texlive-francais-bst
Epoch:		1
Version:	38922
Release:	1
Summary:	Bibliographies conforming to French typographic standards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/francais-bst
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/francais-bst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/francais-bst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides bibliographies (in French) conforming to
the rules in "Guide de la communication écrite" (Malo, M.,
Quebec Amerique, 1996. ISBN 978-2-8903-7875-9) The BibTeX
styles were generated using custom-bib and they are compatible
with natbib.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/francais-bst
%doc %{_texmfdistdir}/doc/bibtex/francais-bst

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
