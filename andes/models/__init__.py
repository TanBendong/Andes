from .jit import JIT


__all__ = ['base',
           'bus',
           ]

order = ['bus', 'Node', 'Ground', 'line',
         'pq', 'pv', 'zone', 'shunt',
         'measurement',
         'synchronous', 'governor', 'avr', 'pss',
         'windturbine', 'wind',
         'coi', 'ACE', 'AGC', 'EAGC',
         'R', 'L', 'C', 'RLs', 'RCs', 'RCp', 'RLCp', 'RLCs', 'DCgen',
         'vsc',
         ]

non_jits = {'bus': {'Bus': 'Bus'},
            'pq': {'PQ': 'PQ'},
            'pv': {'PV': 'PV',
                   'Slack': 'SW'},
            'line': {'Line': 'Line'},
            'shunt': {'Shunt': 'Shunt'},
            'zone': {'Zone': 'Zone',
                     'Area': 'Area',
                     'Region': 'Region',
                     },
            'agc': {'ACE': 'ACE',
                    'AGC': 'AGC',
                    'EAGC': 'EAGC',
                    },
            'coi': {'COI': 'COI',
                    },
            'dcbase': {'Node': 'Node',
                       'Ground': 'Ground',
                       'R': 'R',
                       'L': 'L',
                       'C': 'C',
                       'RLs': 'RLs',
                       'RCs': 'RCs',
                       'RCp': 'RCp',
                       'RLCp': 'RLCp',
                       'RLCs': 'RLCs',
                       'DCgen': 'DCgen',
                       },
            'synchronous': {'Syn2': 'Syn2',
                            'Syn6a': 'Syn6a',
                            },
            'fault': {'Fault': 'Fault'},
            'breaker': {'Breaker': 'Breaker'},
            'governor': {'TG2': 'TG2',
                         'TG1': 'TG1'},
            'measurement':{'BusFreq': 'BusFreq',
                           'PMU': 'PMU',
                           },
            'avr': {'AVR3': 'AVR3',
                    'AVR2': 'AVR2',
                    'AVR1': 'AVR1',
                    },
            'pss': {'PSS1': 'PSS1',
                    'PSS2': 'PSS2',
                    },
           }

jits = {'vsc': {'VSC': 'VSC',
                'VSC1': 'VSC1',
                'VSC2A': 'VSC2A',
                'VSC2B': 'VSC2B'
                },
        'windturbine': {'WTG3': 'WTG3',
                        'WTG4DC': 'WTG4DC',
                        },
        'wind': {'Weibull': 'Weibull',
                 'ConstWind': 'ConstWind'
                 },
        }
