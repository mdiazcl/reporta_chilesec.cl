import mistune

head_html = '<html><head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous"><link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css" integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script><link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css"><script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script><script>$(document).ready( function () { $(\'#listadoEmpresas\').DataTable(); } );</script></head><body><div class="container"><div class="row"><div class="col-md-12"><img src="header.png" width="100%" alt="header" /></div></div><div class="row"><div class="col-md-12"><hr noshade="noshade"></div></div><div class="row"><div class="col-md-12"><hr noshade="noshade"></div></div><div class="row"><div class="col-md-12">'
tail_html = '</div></div></div></body></html>'

markdown = open('data.md', 'r+')
body_html = mistune.markdown(markdown.read())

output = open('index.html', 'w+')
output.seek(0)
output.truncate()
output.write(head_html + body_html + tail_html)

markdown.close()
output.close()