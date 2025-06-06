# Changes to reconcile `rights` semantics of specification and recipe

I believe that the current version of the [Rights Statement](https://iiif.io/api/cookbook/recipe/0008-rights/) does not reflect the intended, if unclear, semantics and use of the [Presentation API v3 `rights` property](https://iiif.io/api/presentation/3.0/#rights).

The intended semantics of the [Presentation API v3 `rights` property](https://iiif.io/api/presentation/3.0/#rights) are that the rights statement URI applies to either the IIIF Resource (read: RDF data described by JSON document) at the place it appears in the Manifest or Collection description, or applies to Content Resources only when added to their descriptions in the JSON (such as use of `rights` in the Image Information).

I note that I was an editor of the unclear Presentation 3 specification and that I approved the [current rights recipe](https://github.com/IIIF/trc/issues/38). I am thus as much to blame as anyone else that it is currently wrong ;-)

## Option 1 - Change recipe to reflect intended semantics

See slides 15-20 in 2025 IIIF Conference presentation ["Open Manifests: Enabling Legal Interoperability and Reuse"](https://docs.google.com/presentation/d/1LJKnwKR8Iec5QgY-pbaZG4Mls2IOPx7D-nNPXJeExsM/edit) which highlights the following issues with the recipe in relation to the intended semantics of `rights`:

> There is a [“Rights Statement”](https://iiif.io/api/cookbook/recipe/0008-rights/) recipe!
> * Repeats Presentation API text that statements are “about a resource (e.g. a Manifest’s JSON or an image’s pixels)”
> * Muddies the differences between rights, requiredStatement and metadata
> * Example has both rights and requiredStatement indicating CC BY-SA

Changes to the [Rights Statement](https://iiif.io/api/cookbook/recipe/0008-rights/) would be:

1. Describe `rights` as applying to the the IIIF Resource, in the example the Manifest JSON, and not the content resources that the Manifest describes. This was the intent of the [Presentation 3 specification definition of `rights`](https://iiif.io/api/presentation/3.0/#rights) even though that is not very clear. See [ongoing specification discussion of how `rights` should be described](https://github.com/IIIF/api/issues/2359).
2. Make a point that what `rights` applies to is not the same as what any human readable rights statement in `requiredStatement` applies to. In the latter the statement is shown with the content resource described by the Manifest and this will be interpreted as applying to that.
3. Change the example to have `rights` as CC0 or such to distinguish it from the rights about the image content which are CC BY-SA as described in `requiredStatement`.

Work for Presentation 4:

* Make the description of `rights` clear about exactly when the rights URI applies to the IIIF Resource (JSON), including what inheritance rules are, and also when the rights URI applies to the Content Resource (Image, etc.) following the description in the Image API.
* Remove the comment about `rights` being "informational".

## Option 2 - Accept that `rights` in Presentation 3 is interpreted as applying to the content resources

Changes to the [Rights Statement](https://iiif.io/api/cookbook/recipe/0008-rights/) would be:

1. Change the description of `rights` to be explicitly about to described Content Resources and accept it as a parallel to `requiredStatement`.

Work for Presentation 4:

* Make the description of `rights` clear that it applied to the Content Resources described by IIIF Resource it is attached to (ie. object described by Manifest if on Manifest resource). Work out where else it should and should not appear.
* Remove the comment about `rights` being "informational".
* Consider whether a new property should be introduced to convey a license about the IIIF Resource content (JSON). Consider inheritance and overrides. Consider whether CC0 might be recommended except in cases where there is creative content such as scholarly annotations.
