"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'ip_reputation_1' block
    ip_reputation_1(container=container)

    return

def ip_reputation_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('ip_reputation_1() called')

    # collect data for 'ip_reputation_1' call

    parameters = []
    
    # build parameters list for 'ip_reputation_1' call
    parameters.append({
        'ip': "8.8.8.8",
    })

    phantom.act("ip reputation", parameters=parameters, assets=['virustotal_tc'], callback=ip_reputation_1_callback, name="ip_reputation_1")

    return

def ip_reputation_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('ip_reputation_1_callback() called')
    
    geolocate_ip_1(action=action, success=success, container=container, results=results, handle=handle)

    return

def geolocate_ip_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('geolocate_ip_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'geolocate_ip_1' call

    parameters = []
    
    # build parameters list for 'geolocate_ip_1' call
    parameters.append({
        'ip': "4.4.4.4",
    })

    phantom.act("geolocate ip", parameters=parameters, assets=['maxmind'], name="geolocate_ip_1", parent_action=action)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions 
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return