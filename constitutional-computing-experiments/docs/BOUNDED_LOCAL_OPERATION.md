# Bounded local operation

The v0.5 experiment evaluated whether ordinary local actions could proceed within previously assigned bounds without consulting a root authority for every action.

Here, a root authority is a central authority that may retain responsibilities beyond an ordinary local action. Previously assigned authority gives local operation a defined boundary; it does not remove that boundary.

## Experimental properties

The frozen experimental record reports:

- Ordinary local actions operated within previously assigned bounds.
- Root-offline local operation was tested within those existing bounds.
- Changing actor or session labels did not reset the bound.
- Ordinary local operation did not require a root consultation for every action in the tested setting.

The root may remain necessary for allocation or coordination outside ordinary local action. Local progress within an existing bound does not establish that new authority is available when root cannot be consulted.

## Interpretation

The experiment distinguishes consulting a central authority for each ordinary action from operating locally under authority assigned beforehand.

That distinction is limited to the tested bounded case. It does not establish that all operations can continue during disconnection, that root is unnecessary, or that authorities can be treated as untrusted.

Trusted local authorities, trusted resource state and conforming writers remain assumptions. The observed behavior is an experimental property, not a description of how authority is moved between authorities.
