from __future__ import print_function  # In python 2.7
from flask import Flask, render_template, request
# from flask_jsglue import JSGlue

###########
# APP CFG #
###########
app = Flask(__name__)
# jsglue = JSGlue(app)
# socketio = SocketIO(app, engineio_logger=DEBUG_ENGINEIO)

# ##########
# # ROUTES #
# ##########

# @app.route('/', methods=['GET'])
# def index():
#     return render_template(
#                 'index.html',
#                 app_name=app_name,
#                 user=user,
#                 domains=DOMAINS,
#                 environs=ENVIRONMENTS,
#                 actions=ACTIONS)


# #############
# # SOCKET IO #
# #############


# @socketio.on('get_clusters', namespace='/clusters')
# def get_clusters(domain):
#     namespace = '/clusters'
#     flask_context = get_flask_context(app, request, request.sid, namespace)
#     # Launch cmd on domain to gather cluster list
#     cmd = build_fab_cmd(
#                 action='wls_cluster_list',
#                 domains=domain,
#                 environs='DEV0',
#                 clusters=None)
#     # Execute command in a thread
#     print("Executing %s" % cmd)
#     t = CommandExecutor(
#             cmd=cmd,
#             data={'domain': domain},
#             flask_context=flask_context)
#     t.start()


# @socketio.on('stream', namespace='/display')
# def stream(data):
#     global t
#     namespace = '/display'
#     actions = data['actions']
#     domains = ';'.join(data['domains'])
#     environs = ';'.join(data['environs'])
#     clusters = ';'.join(data['clusters'])
#     flask_context = get_flask_context(app, request, request.sid, namespace)

#     # For each action, execute cmd, stream cmd output, parse output
#     for action in actions:
#         cmd = build_fab_cmd(
#                     action=action,
#                     environs=environs,
#                     domains=domains,
#                     clusters=clusters)

#         print("Executing %s" % cmd)
#         t = CommandExecutor(
#                 cmd=cmd,
#                 flask_context=flask_context,
#                 data={'action': action})
#         t.start()


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
