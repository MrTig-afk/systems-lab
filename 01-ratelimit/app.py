'''
is_allowed(client_id, now, state, limit=5, window_seconds=60)

- client_id: a string identifying who's making the request (e.g. "user_42")
- now: a number — the current time in seconds. This is NOT read from a real
  clock inside your function. It's always passed in by whoever calls the
  function.
- state: a dictionary you use to remember, across repeated calls, how many
  requests each client has made and when their current window started. You
  design its internal shape yourself.
- limit: max requests allowed per window (default 5)
- window_seconds: length of one window, in seconds (default 60)

Returns True if this request should be allowed, False if the client has
exceeded their limit for the current window.

'''

def is_allowed(client_id, now, state, limit=5, window_seconds=60):

    current_window= now//window_seconds # to compute which window it is in per second
    updated= state.get(client_id,{"count":0, "window":0})
    if updated["window"] == current_window:
        if updated['count'] < limit:
            updated['count'] += 1
            state[client_id] = updated #idk how this works tbvh, the reverse isnt going to my head
            return True

            #idk how to add it into state afterwards
        else:
           return False
    else:
       updated["window"] = current_window
       updated["count"] = 1
       state[client_id] = updated #idk how this works tbvh, the reverse isnt going to my head
       return True

       # still dont know how to update to state, also how and when do we initialize state? I assume that us writing state, is already initializing it
        

# tests
state = {}

# 5 calls within the same window
for i in range(5):
    result = is_allowed("user_45", 45, state, 3, 60)
    print(result)

# One call after the window has expired
result = is_allowed("user_45", 115, state, 3, 60)
print(result)