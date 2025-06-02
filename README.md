# IIIF Open Metadata

## A sampling of IIIF Collections

This sample is taken from the [Guides to finding IIIF resources](https://iiif.io/guides/finding_resources/) as of 2025-06-02 and I attempt to find one manifest from each listed collection.

* Bavarian State Library (BSB) / Munich Digitization Centre (MDZ)
  * https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11853734/manifest
* Bibliothèque nationale de France (BnF)
  * https://gallica.bnf.fr/iiif/ark:/12148/bpt6k6564680d/manifest.json
* Biblissima
  * https://gallica.bnf.fr/iiif/ark:/12148/btv1b9061241w/manifest.json
* Blavatnik Archive
  * https://www.blavatnikarchive.org/api/data/es/iiif-manifest/10133?type=mirador&site=baf
* Bodmer Lab
  * https://iiif.unige.ch/manifest/IIIFManifest_1072068799.json
* British Library - FIXME, link is broken
* Brown University Digital Repository
  * https://repository.library.brown.edu/iiif/presentation/bdr:37024/manifest.json
* Cardiff University
  * https://librarysearch.cardiff.ac.uk/view/iiif/presentation/44WHELF_CAR/12204338230002420/manifest?iiifVersion=2
* Cultural Japan
  * https://api.cultural.jp/iiif/metmuseum-78663/manifest
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
  * https://e-codices.ch/metadata/iiif/zhl-P0013-2-1/manifest.json
* e-manuscripta (Manuscript material from Swiss libraries and archives)
  * https://www.e-manuscripta.ch/i3f/v20/4602948/manifest
* e-rara (digitized rare books from Swiss institutions)
  * https://www.e-rara.ch/i3f/v20/7568336/manifest
* Ecole Polytechnique Fédérale de Lausanne (EPFL) - SEEMS BROKEN
* Europeana - BROKEN, 503, try https://www.europeana.eu/en/item/09403/o_gm_1671_CHO
* Folger Shakespeare Library - LINK NEED UPDATING TO NEW SYSTEM
  * https://digitalcollections.folger.edu/node/50479/manifest
* Fragmentarium - Digital Research Laboratory for Medieval Manuscript Fragments
  * https://fragmentarium.ms/metadata/iiif/F-qdm5/manifest.json
* Ghent University
  * https://adore.ugent.be/IIIF/v3/manifests/archive.ugent.be:ACB41F1C-F681-11E9-9639-C36B765DA7FD
* Guide to IIIF personas - WHY IS THIS IN THIS LIST?
* Göttingen University Collections
  * https://manifests.sub.uni-goettingen.de/iiif/presentation/PPN235181684_0029/manifest?version=7a696723
* Harvard Art Museum
  * https://iiif.harvardartmuseums.org/manifests/object/133370
* Harvard University Digital Collections - BROKEN LINK
* Huntington Digital Library
  * https://hdl.huntington.org/iiif/2/p15150coll7:5145/manifest.json
* Indigenous Digital Archive - MESSAGE SAYING TEMPORARILY OFFLINE
* Internet Archive
  * https://iiif.archive.org/iiif/b29000427_0001/manifest.json
* J. Paul Getty Trust
  * https://media.getty.edu/iiif/manifest/bff54470-38c3-4865-bd58-b550f19b715e
* KU Leuven - LINK NEEDS UPDATE? https://kuleuven.limo.libis.be/discovery/search?vid=32KUL_KUL:KULeuven, can't fine Manifest URIs from Teneo, e.g. https://repository.teneo.libis.be/delivery/DeliveryManagerServlet?dps_pid=IE40152947&
* Lancaster University Library
  * https://digitalcollections.lancaster.ac.uk/iiif/MS-DAVY-10600
* Leiden University
  * https://digitalcollections.universiteitleiden.nl/iiif_manifest/item%3A360423/manifest
* Library of Congress
  * https://www.loc.gov/item/2015561754/manifest.json
* National Gallery of Art Library
  * https://libraryimage.nga.gov/manifest/mms/994332947304896.json
* National Library of Scotland - DON'T FIND IIIF, e.g. https://digital.nls.uk/lewis-grassic-gibbon-books/archive/205174244
* National Library of Wales
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

While the [2.0 to 3.0 Changle Log](https://iiif.io/api/presentation/3.0/change-log/#125-rename-license-to-rights) does note the change from `license` to `rights` for the property name, and the ability to specify multiple values, it does not discuss the change in semantics to possibly apply to the JSON Manifest.

Image - https://iiif.io/api/image/3.0/#56-rights

Text is specific that the license applies to the pixels of the image. Thus, one can also  and, additionally, the way to do this in the presentation API is to add t `rights` to the Image service description:

Cookbook example "https://iiif.io/api/cookbook/recipe/0008-rights/" repeats the Presentation 3.0 specification text but adds no clarity as to whether the `rights` property applies to the JSON Manifest or the resource it represents.

### Image and Presentation 2.0 - `license`

Presentation - https://iiif.io/api/presentation/2.0/#rights-and-licensing-properties

Text is very unclear: _"A link to an external resource that describes the license or rights statement under which the resource is being used."_

The [Image API 2.0](https://iiif.io/api/image/2.0/) does not include properties for expressing rights information. The text explains that the Image API did not support rights information: _"This specification makes no assertion about the rights status of requested images or any other descriptive metadata, whether or not authentication has been accomplished. Please see the IIIF Presentation API for rights and other information."_
