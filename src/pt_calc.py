import tkinter as tk
from datetime import datetime, timedelta
import gettext

# --- internationalization ---
#gettext.install(domain="interpy", localedir="locales")

#to test specific language here
gettext.translation(
    "messages",
    localedir="locales",
    languages=["fr"],
    fallback=True
).install()


def get_time(actual_pts, needed_pts, time_for_pt):
    missing_pts = max(0, needed_pts - actual_pts)
    total_minutes = missing_pts * time_for_pt

    final_hours = int(total_minutes // 60)
    final_minutes = int(total_minutes % 60)

    time_charged = datetime.now() + timedelta(minutes=total_minutes)

    return final_hours, final_minutes, time_charged

def my_time_calculator():
    try:
        actual_pts = float(entry_actual.get())
        needed_pts = float(entry_needed.get())
        time_for_pt = float(entry_time.get())  # in minutes

        final_hours, final_minutes, time_charged = get_time(actual_pts, needed_pts, time_for_pt)

        label_result.config(text=
                            _("You'll have to wait %(hours)d hours and %(minutes)d minutes. "
                              "Your points will be charged at %(time)s") % 
                              {
                                "hours": final_hours,
                                "minutes": final_minutes,
                                "time": time_charged.strftime('%H:%M')
                              }
                            )
    except ValueError:
        label_result.config(text=_("Input not valid. Please enter numeric values."))

# UI
if __name__ == "__main__":
    root = tk.Tk()
    root.title(_("Point Time Calculator"))

    tk.Label(root, text=_("Your current Points:")).grid(row=0, column=0)
    tk.Label(root, text=_("Your needed Points:")).grid(row=1, column=0)
    tk.Label(root, text=_("Recharge time for one point (in minutes):")).grid(row=2, column=0)

    entry_actual = tk.Entry(root)
    entry_needed = tk.Entry(root)
    entry_time = tk.Entry(root)

    entry_actual.grid(row=0, column=1)
    entry_needed.grid(row=1, column=1)
    entry_time.grid(row=2, column=1)

    tk.Button(root, text=_("Calculate"), command=my_time_calculator).grid(row=3, column=0, columnspan=2)

    label_result = tk.Label(root, text="")
    label_result.grid(row=4, column=0, columnspan=2)

    root.mainloop()