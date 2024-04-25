import unreal
import importlib
from Lib import __lib_topaz__ as topaz


# rotation Z
actors = topaz.get_selected_level_actors()

for actor in actors:
    rot = actor.get_actor_rotation()
    rot.yaw += 90
    actor.set_actor_rotation(rot, True)
    