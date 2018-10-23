# Documentation: https://wfdb.readthedocs.io/en/latest/plot.html
import wfdb

record = wfdb.rdrecord('mitdb/100', sampto=3000)
ann = wfdb.rdann('mitdb/100', 'atr', sampto=3000)

wfdb.plot_items(signal=record.p_signal,
                ann_samp=[ann.sample, ann.sample],
                title='MIT-BIH Record 100', time_units='seconds',
                figsize=(10,4), ecg_grids='all')

# wfdb.plot_wfdb(record=record, annotation=ann, plot_sym=True,
#                time_units='seconds', title='MIT-BIH Record 100',
#                figsize=(10,4), ecg_grids='all')

# wfdb.plot.plot_all_records(directory='mitdb')