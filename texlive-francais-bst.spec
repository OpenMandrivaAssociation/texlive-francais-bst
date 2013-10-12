# revision 30446
# category Package
# catalog-ctan /biblio/bibtex/contrib/francais-bst
# catalog-date 2013-05-12 22:32:31 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-francais-bst
Epoch:		1
Version:	1.1
Release:	1
Summary:	Bibliographies conforming to French typographic standards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/francais-bst
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/francais-bst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/francais-bst.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides bibliographies (in French) conforming to
the rules in "Guide de la communication ecrite" (Malo, M.,
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
%{_texmfdistdir}/bibtex/bst/francais-bst/francais.bst
%{_texmfdistdir}/bibtex/bst/francais-bst/francaissc.bst
%doc %{_texmfdistdir}/doc/bibtex/francais-bst/README
%doc %{_texmfdistdir}/doc/bibtex/francais-bst/francaisbst.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
