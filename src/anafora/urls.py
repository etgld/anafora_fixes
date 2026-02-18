from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r"^getDir/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<isAdj>Adjudication))?/view(?:/(?P<crossDoc>_crossDoc))?/?$",
        views.getAllTask,
    ),
    # views.getAllTask),
    # re_path(r'^getDir/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?\.Adjudication(?:/(?P<crossDoc>_crossDoc))?/?$', views.getAdjudicationTaskFromProjectCorpusName),
    re_path(
        r"^getDir/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?\.Adjudication(?:/(?P<crossDoc>_crossDoc))?/?$",
        views.getAdjudicationTaskFromProjectCorpusName,
    ),
    # re_path(r'^getDir/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?\.Adjudication/?$', views.getAdjudicationTaskFromProjectCorpusName),
    re_path(
        r"^getDir/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<parentTaskName>[^\/]+)/_cross/?$",
        views.getSubTaskFromProjectCorpusTaskName,
    ),
    re_path(
        r"^getDir/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:/(?P<crossDoc>_crossDoc))?/?$",
        views.getTaskFromProjectCorpusName,
    ),
    re_path(r"^getDir/(?P<projectName>[^\/]+)/?$", views.getCorpusFromProjectName),
    re_path(r"^getDir/?$", views.getProject),
    re_path(
        r"^xml/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^.]*))?\.(?P<isAdj>Adjudication)(?:/_sub_(?P<subTaskName>[^\/]+))?/?$",
        views.getAnaforaXMLFile,
    ),
    re_path(
        r"^xml/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^.]*))?\.(?P<isAdj>Adjudication)/(?P<annotatorName>[^\/]+)(?:/_sub_(?P<subTaskName>[^\/]+))?/?$",
        views.getAnaforaXMLFile,
    ),
    re_path(
        r"^xml/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:/_sub_(?P<subTaskName>[^\/]+))?/?$",
        views.getAnaforaXMLFile,
    ),
    re_path(
        r"^xml/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?/(?P<annotatorName>[^\/]+)(?:/_sub_(?P<subTaskName>[^\/]+))?/?$",
        views.getAnaforaXMLFile,
    ),
    re_path(
        r"^completeAnnotator/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<isAdj>Adjudication))?/?$",
        views.getCompleteAnnotator,
    ),
    re_path(
        r"^inprogressAnnotator/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<isAdj>Adjudication))?/?$",
        views.getInprogressAnnotator,
    ),
    re_path(
        r"^annotator/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<isAdj>Adjudication))?/?$",
        views.getAnnotator,
    ),
    re_path(r"^schema/(?P<schema>[^\/]+)/(?P<schemaIdx>[0-9]+)/?$", views.getSchema),
    re_path(r"^schema/(?P<schema>[^\/]+)/?$", views.getSchema),
    re_path(
        r"^saveFile/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<isAdj>Adjudication))?/?$",
        views.writeFile,
    ),
    re_path(
        r"^saveFile/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<isAdj>Adjudication))?/?$",
        views.writeFile,
    ),
    re_path(
        r"^setCompleted/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<isAdj>Adjudication))?/?$",
        views.setCompleted,
    ),
    re_path(
        r"^setCompleted/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<isAdj>Adjudication))?/?$",
        views.setCompleted,
    ),
    re_path(
        r"^logging/(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schemaName>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<isAdj>Adjudication))?/?$",
        views.saveLogging,
    ),
    re_path(
        r"^(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schema>[^\/\.]+)(?:\.(?P<schemaMode>[^\/A-Za-z0-9\.]*))?(?:\.(?P<adjudication>Adjudication))?(?:\/(?P<view>view))?(?:/(?P<crossDoc>_crossDoc))?(?:\/(?P<logging>_logging_))?(?:\/(?P<annotator>[^\/]+))?/?$",
        views.annotateNormal,
    ),
    re_path(
        r"^(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/(?P<taskName>[^\/]+)/(?P<schema>[^\/\.]+)(?:\.(?P<schemaMode>[^\/\.]+))?(?:\.(?P<adjudication>Adjudication))?(?:\/(?P<view>view))?(?:/(?P<crossDoc>_crossDoc))?(?:\/(?P<logging>_logging_))?(?:\/(?P<annotator>[^\/]+))?/?$",
        views.annotateNormal,
    ),
    re_path(r"^(?P<projectName>[^\/]+)/(?P<corpusName>[^\/]+)/?$", views.selectCorpus),
    re_path(r"^(?P<projectName>[^\/]+)/?$", views.selectProject),
    re_path(r"^$", views.index),
]
# + static(settings.STATIC_URL, documeent_root=settings.STATIC_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
