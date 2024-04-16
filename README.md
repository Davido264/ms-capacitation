# Setup
```sh
python -m venv .venv
source .venv/bin/activate

git submodule update --init --depth 1
python -m pip install -r requirements.txt

# For non nix setup
pg_ctl -s init -o "-E UTF-8 --no-locale -A trust" -D $PGDATA

# For some reason, I don't have /run/postgresql/ and postgres fails
sudo mkdir -p /run/postgresql/ && sudo chown $USER /run/postgresql/

postgres --single -D "$PGDATA" postgres < "prepare.sql" >/dev/null

./odoo/odoo-bin -c odoo/odoo.conf
```
