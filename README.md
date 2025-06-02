# IIIF Open Metadata

## A sampling of IIIF Collections

This sample is taken from the [Guides to finding IIIF resources](https://iiif.io/guides/finding_resources/) as of 2025-06-02 and I attempt to find one manifest from each listed collection.

* Bavarian State Library (BSB) / Munich Digitization Centre (MDZ)
x  * https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11853734/manifest
* Bibliothèque nationale de France (BnF)
x  * https://gallica.bnf.fr/iiif/ark:/12148/bpt6k6564680d/manifest.json
* Biblissima
x  * https://gallica.bnf.fr/iiif/ark:/12148/btv1b9061241w/manifest.json
* Blavatnik Archive
x  * https://www.blavatnikarchive.org/api/data/es/iiif-manifest/10133?type=mirador&site=baf
* Bodmer Lab
x  * https://iiif.unige.ch/manifest/IIIFManifest_1072068799.json
* British Library - FIXME, link is broken
* Brown University Digital Repository
x  * https://repository.library.brown.edu/iiif/presentation/bdr:37024/manifest.json
* Cardiff University
x  * https://librarysearch.cardiff.ac.uk/view/iiif/presentation/44WHELF_CAR/12204338230002420/manifest?iiifVersion=2
* Cultural Japan
x  * https://api.cultural.jp/iiif/metmuseum-78663/manifest
* David Rumsey Map Collection
  * https://www.davidrumsey.com/luna/servlet/iiif/m/RUMSEY~8~1~305961~90076345/manifest
* Digital Commonwealth
  * https://www.digitalcommonwealth.org/search/commonwealth:668305767/manifest
    * Seems a clear indication that the `license` property on the `Manifest` object is being used to indicate the rights information for the image content:
    ```
    "attribution": "Rights status not evaluated. This work is licensed for use under a Creative Commons Attribution Non-Commercial No Derivatives License (CC BY-NC-ND).",
    "license": "http://creativecommons.org/licenses/by-nc-nd/4.0/"
    ```
* Digital Repository of Ireland
  * https://repository.dri.ie/iiif/collection/b564jg065.json
* Durham University
  * https://iiif.durham.ac.uk/manifests/trifle/32150/t1/mv/t1/t1mvt150j86r/manifest
* e-codices - Virtual Manuscript Library of Switzerland

e-manuscripta (Manuscript material from Swiss libraries and archives)
e-rara (digitized rare books from Swiss institutions)
Ecole Polytechnique Fédérale de Lausanne (EPFL)
Europeana
Folger Shakespeare Library
Fragmentarium - Digital Research Laboratory for Medieval Manuscript Fragments
Ghent University
Guide to IIIF personas
Göttingen University Collections
Harvard Art Museum
Harvard University Digital Collections
Huntington Digital Library
Indigenous Digital Archive
Internet Archive
J. Paul Getty Trust
KU Leuven
Lancaster University Library
Leiden University
Library of Congress
National Gallery of Art Library
National Library of Scotland
National Library of Wales
National Palace Museum (Taiwan)
North Carolina State University Libraries
Northwestern University
Parliamentary Archives - UK
Princeton University Art Museum
Princeton University Libraries
Qatar National Library
Radboud University Library
Smithsonian Institution
Smithsonian National Zoo
Stanford University
UCLA Library Digital Collections
Universitaet Jena
University College Dublin Libraries
University of Cambridge
University of Leicester Library
University of North Texas Libraries
University of Oxford (Digital Bodleian)
University of St. Andrews
University of Toronto
University of Washington Libraries
Using the navPlace Extension With Leaflet
Utrecht University Library
Vatican Library
Villanova University
Wellcome Collection
Wikidata
Wikipedia
World Digitial Library
Yale Center for British Art
Yale Peabody Museum
Yale University Art Gallery
Yale University Library

## Rights properties

### Image and Presentation 3.0 - `rights`

Presentation - https://iiif.io/api/presentation/3.0/#rights

Text is quite clear that the rights information applies to the IIIF context resource that may be the JSON of the Manifest: _"A string that identifies a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image."_

Image - https://iiif.io/api/image/3.0/#56-rights

Text is specific that the license applies to the pixels of the image and, additionally, the way to do this in the presentation API is to add the `license` to the Image service description:

```

```

### Image and Presentation 2.0 - `license`

Presentation - https://iiif.io/api/presentation/2.0/#rights-and-licensing-properties

Text is very unclear: _"A link to an external resource that describes the license or rights statement under which the resource is being used."_

The [Image API 2.0](https://iiif.io/api/image/2.0/) does not include properties for expressing rights information. The text explains that the Image API did not support rights information: _"This specification makes no assertion about the rights status of requested images or any other descriptive metadata, whether or not authentication has been accomplished. Please see the IIIF Presentation API for rights and other information."_
