```bash
odoo.py scaffold <"module name"> <"where to put it">
```


# Composition
- Bussiness objects: Python classes
- Data files: XML or csv
- Web controllers
- Static web data: assets, styles and js

# Key points
- MVC structure
- Relies on an `__manifest__.py` file to declare its existance to the system
- Its ORM is similar to Djangos with some key differences

---

## ORM
- Must have a `_name` property, mainly for metadata purposes.
    - Also, `name` is required for UI behaviours
```python
from openerp import models,fields

class Cow:
    _name: "cowsay.cow"

    name : fields.Char(string="cow_name", required=True, index=True, help="Name of this dude")
    eyes : fields.Char(help="Eye style")
    think: fields.Boolean(help="Wether is thinking or saying")
    schedule: fields.Date(required=True, index=True)
```
- Arguments of `fields` classes are:
    - `string`. Tells the label of the field in the UI
    - `required`. Wether is optional or not
    - `index`. Wether create a db index over the field, or not
    - `help`. Additional information

- Other things to consider
    - `id`, `create_date`, `write_date`, `create_uid`, `write_uid` are created dynamically, therefore this properties are reserverd

## Actual data
- Declared in XML files (JDSL vibes)
```xml
<openerp>
    <data>
        <record mode="cowsay.cow" id="cow0">
            <field name="cow_name">Hector</field>
            <field name="eyes">00</field>
            <field name="think">false</field>
            <field name="schedule"></field>
        <record>
    </data>
</openerp>
```

## Actions
- Actions can trigger python code or spawn new UI elements
- For new UI elements, actions are defined in XML too
```xml
<record model="ir.actions.act_window" id="cowsay">
    <field name="name">Name of Cow</field>
    <field name="res_model">cow.cow</field>
    <field name="view_model">tree,form</field>
</record>
<menuitem id="menu_cows" parent="menu_root" name="Cows" sequence="10" action="cowsay"/>
```

## Views
- Views use the XML datalanguage as a DSL to build UI elements
- They follow the `<record>` and `<field>` structure in that way, child elements or additional propts are set
- For example this...
```js
import { View } from "ir.ui"
const app = () =>
    <View id="some_id" foo="bar" fiz="buz">
        <Form>
            <Tree id="tree_id" />
        </Form>
    </View>
```
- Is the same as this...
```XML
<record model="ir.ui.view" id="some_id">
    <field name="foo">bar</field>
    <field name="fiz">buz</field>
    <field name="arch" type="xml">
        <form>
            <tree id="tree_id">
            </tree>
        </form>
    </field>
</record>
```
- `type="xml"` must be present when declaring a field named `arch`
- some components that are available are `tree`, `notebook`, `form` and `search`

## Relationship
- when using `fields` One can use special clases to define foreign keys and relations
- parameters in this clases takes an `str` which has to be the `_name` of the entity is related to. Also takes an `on_delete` parameter, similar to SQL
```python
class CowOwner:
    _name: "cowsay.cow_owner"

    name : fields.Char(required=True, index=True, help="Name of this dude")
    cows : fields.OneToMany("cowsay.cow", on_delete="cascade")
```

## Inheritance
- Se puede aplicar herencia en modelos y en vistas.
- Se utiliza `_inherit = "model.model"` para especificar herencia tradicional
- Se utiliza `_inherits = "model.model"` para especificar herencia por composición

## View Inheritance
- `<field name="inherit_id" ref="<id>"/>`
- Inside `<field name="arch" type="xml">` there are elements of type `<xpath>`
```xml
<record id="idea_category_list2" model="ir.ui.view">
    <field name="name">id.category.list2</field>
    <field name="model">idea.category</field>
    <field name="inherit_id" ref="id_category_list"/>
    <field name="arch" type="xml">
        <!-- find field description and add the field
             idea_ids after it -->
        <xpath expr="//field[@name='description']" position="after">
          <field name="idea_ids" string="Number of ideas"/>
        </xpath>
    </field>
</record>
```
- `xpath` has an attribute `expr`, which is an xml query expression, and `position`, which is the operation to apply to the matched element

## Domains
- `field` classes has also domains to define constraints
```python
    foo : fields.Many2one("res.partner",domain=["&",("foo","=",True),("bar","ilike","faz")])
```



