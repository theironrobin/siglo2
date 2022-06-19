pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'siglo2')
gnome = import('gnome')

gnome.compile_resources('siglo2',
  'siglo2.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'siglo2.in',
  output: 'siglo2',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

siglo2_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(siglo2_sources, install_dir: moduledir)
