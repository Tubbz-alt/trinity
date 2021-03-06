Command Line Interface (CLI)
============================

The following is a brief description of all the configurations available on the command line.
We can also generate an always up-to-date version of them by running ``trinity --help``.

.. code-block:: shell

    usage: trinity [-h] [--version] [--trinity-root-dir TRINITY_ROOT_DIR]
                   [--port PORT] [--trinity-tmp-root-dir] [-l LEVEL]
                   [--stderr-log-level STDERR_LOG_LEVEL]
                   [--file-log-level FILE_LOG_LEVEL]
                   [--network-id NETWORK_ID | --ropsten | --goerli]
                   [--preferred-node PREFERRED_NODES] [--max-peers MAX_PEERS]
                   [--genesis GENESIS] [--data-dir DATA_DIR] [--nodekey NODEKEY]
                   [--profile] [--disable-rpc]
                   [--enable-http-apis ENABLE_HTTP_APIS]
                   [--http-listen-address HTTP_LISTEN_ADDRESS]
                   [--http-port HTTP_PORT]
                   [--network-tracking-backend {sqlite3,memory,do-not-track}]
                   [--disable-networkdb-component] [--disable-blacklistdb]
                   [--disable-eth1-peer-db]
                   [--enable-experimental-eth1-peer-tracking]
                   [--disable-discovery] [--disable-upnp] [--enable-ethstats]
                   [--ethstats-server-url ETHSTATS_SERVER_URL]
                   [--ethstats-server-secret ETHSTATS_SERVER_SECRET]
                   [--ethstats-node-id ETHSTATS_NODE_ID]
                   [--ethstats-node-contact ETHSTATS_NODE_CONTACT]
                   [--ethstats-interval ETHSTATS_INTERVAL] [--enable-metrics]
                   [--metrics-host METRICS_HOST]
                   [--metrics-influx-user METRICS_INFLUX_USER]
                   [--metrics-influx-database METRICS_INFLUX_DATABASE]
                   [--metrics-influx-password METRICS_INFLUX_PASSWORD]
                   [--metrics-influx-server METRICS_INFLUX_SERVER]
                   [--metrics-influx-port METRICS_INFLUX_PORT]
                   [--metrics-influx-protocol METRICS_INFLUX_PROTOCOL]
                   [--metrics-reporting-frequency METRICS_REPORTING_FREQUENCY]
                   [--metrics-system-collector-frequency METRICS_SYSTEM_COLLECTOR_FREQUENCY]
                   [--metrics-blockchain-collector-frequency METRICS_BLOCKCHAIN_COLLECTOR_FREQUENCY]
                   [--disable-request-server]
                   [--sync-mode {header,full,beam,light,none}]
                   [--sync-from-checkpoint SYNC_FROM_CHECKPOINT]
                   [--disable-backfill]
                   [--force-beam-block-number FORCE_BEAM_BLOCK_NUMBER]
                   [--disable-tx-pool]
                   {attach,db-shell,fix-unclean-shutdown,remove-network-db,export,import}
                   ...

    Trinity

    positional arguments:
      {attach,db-shell,fix-unclean-shutdown,remove-network-db,export,import}
        attach              open an REPL attached to a currently running chain
        db-shell            open a REPL to inspect the db
        fix-unclean-shutdown
                            close any dangling processes from a previous unclean
                            shutdown
        remove-network-db   Remove the on-disk sqlite database that tracks data
                            about the p2p network
        export              Export blocks to a file (RLP encoded)
        import              Import blocks from a file (RLP encoded)

    optional arguments:
      -h, --help            show this help message and exit
      --disable-rpc         Disables the JSON-RPC server
      --enable-http-apis ENABLE_HTTP_APIS
                            Enable HTTP access to specified JSON-RPC APIs (e.g.
                            'eth,net'). Use '*' to enable HTTP access to all
                            modules (including eth_admin).

      --http-listen-address HTTP_LISTEN_ADDRESS
                            Address for the HTTP server to listen on
      --http-port HTTP_PORT
                            JSON-RPC server port
      --disable-discovery   Disable peer discovery
      --disable-upnp        Disable upnp mapping
      --disable-request-server
                            Disables the Request Server
      --disable-tx-pool     Disables the Transaction Pool

    core:
      --version             show program's version number and exit
      --trinity-root-dir TRINITY_ROOT_DIR
                            The filesystem path to the base directory that trinity
                            will store it's information. Default:
                            $XDG_DATA_HOME/.local/share/trinity
      --port PORT           Port on which trinity should listen for incoming
                            p2p/discovery connections. Default: 30303
      --trinity-tmp-root-dir
                            If this flag is set, trinity will launch with a
                            temporary root directory as provided by the
                            ``tempfile`` library.

    logging:
      -l LEVEL, --log-level LEVEL
                            Configure the logging level. LEVEL must be one of:
                            8/10/20/30/40/50 (numeric);
                            debug2/debug/info/warn/warning/error/critical
                            (lowercase);
                            DEBUG2/DEBUG/INFO/WARN/WARNING/ERROR/CRITICAL
                            (uppercase).
      --stderr-log-level STDERR_LOG_LEVEL
                            Configure the logging level for the stderr logging.
      --file-log-level FILE_LOG_LEVEL
                            Configure the logging level for file-based logging.

    network:
      --network-id NETWORK_ID
                            Network identifier (1=Mainnet, 3=Ropsten)
      --ropsten             Ropsten network: pre configured proof-of-work test
                            network. Shortcut for `--networkid=3`
      --goerli              Goerli network: pre configured proof-of-authority
                            (Clique) test network. Shortcut for `--networkid=5`
      --preferred-node PREFERRED_NODES
                            An enode address which will be 'preferred' above nodes
                            found using the discovery protocol
      --max-peers MAX_PEERS
                            Maximum number of network peers

    chain:
      --genesis GENESIS     File containing a custom genesis configuration file
                            per EIP1085
      --data-dir DATA_DIR   The directory where chain data is stored
      --nodekey NODEKEY     Hexadecimal encoded private key to use for the nodekey
                            or the filesystem path to the file which contains the
                            nodekey

    debug:
      --profile             Enables profiling via cProfile.

    network db:
      --network-tracking-backend {sqlite3,memory,do-not-track}
                            Configure whether nodes are tracked and how. (sqlite3:
                            persistent tracking across runs from an on-disk
                            sqlite3 database, memory: tracking only in memory, do-
                            not-track: no tracking)
      --disable-networkdb-component
                            Disables the builtin 'Network Database' component.
                            **WARNING**: disabling this API without a proper
                            replacement will cause your trinity node to crash.
      --disable-blacklistdb
                            Disables the blacklist database server component of
                            the Network Database component. **WARNING**: disabling
                            this API without a proper replacement will cause your
                            trinity node to crash.
      --disable-eth1-peer-db
                            Disables the ETH1.0 peer database server component of
                            the Network Database component. **WARNING**: disabling
                            this API without a proper replacement will cause your
                            trinity node to crash.
      --enable-experimental-eth1-peer-tracking
                            Enables the experimental tracking of metadata about
                            successful connections to Eth1 peers.

    ethstats (experimental):
      --enable-ethstats     Enable node stats reporting service
      --ethstats-server-url ETHSTATS_SERVER_URL
                            Node stats server URL (e. g. wss://example.com/api)
      --ethstats-server-secret ETHSTATS_SERVER_SECRET
                            Node stats server secret
      --ethstats-node-id ETHSTATS_NODE_ID
                            Node ID for stats server
      --ethstats-node-contact ETHSTATS_NODE_CONTACT
                            Node contact information for stats server
      --ethstats-interval ETHSTATS_INTERVAL
                            The interval at which data is reported back

    metrics:
      --enable-metrics      Enable metrics component
      --metrics-host METRICS_HOST
                            Host name to tag the metrics data (e.g. trinity-
                            bootnode-europe-pt)
      --metrics-influx-user METRICS_INFLUX_USER
                            Influx DB user. Defaults to `trinity`
      --metrics-influx-database METRICS_INFLUX_DATABASE
                            Influx DB name. Defaults to `trinity`
      --metrics-influx-password METRICS_INFLUX_PASSWORD
                            Influx DB password. Defaults to ENV var
                            TRINITY_METRICS_INFLUX_DB_PW
      --metrics-influx-server METRICS_INFLUX_SERVER
                            Influx DB server. Defaults to ENV var
                            TRINITY_METRICS_INFLUX_DB_SERVER
      --metrics-influx-port METRICS_INFLUX_PORT
                            Influx DB port. Defaults to ENV var
                            TRINITY_METRICS_INFLUX_DB_PORT or 8086
      --metrics-influx-protocol METRICS_INFLUX_PROTOCOL
                            Influx DB protocol. Defaults to ENV var
                            TRINITY_METRICS_INFLUX_DB_PROTOCOL or http
      --metrics-reporting-frequency METRICS_REPORTING_FREQUENCY
                            The frequency in seconds at which metrics are reported
      --metrics-system-collector-frequency METRICS_SYSTEM_COLLECTOR_FREQUENCY
                            The frequency in seconds at which system metrics are
                            collected
      --metrics-blockchain-collector-frequency METRICS_BLOCKCHAIN_COLLECTOR_FREQUENCY
                            The frequency in seconds at which blockchain metrics
                            are collected

    sync mode:
      --sync-mode {header,full,beam,light,none}
      --sync-from-checkpoint SYNC_FROM_CHECKPOINT
                            Start syncing from a trusted checkpoint specified
                            using URI syntax:By specific block,
                            eth://block/byhash/<hash>?score=<score>Let etherscan
                            pick a block near the tip,
                            eth://block/byetherscan/latest
      --disable-backfill    Disable backfilling of headers (introduced through
                            checkpointing)
      --force-beam-block-number FORCE_BEAM_BLOCK_NUMBER
                            Force beam sync to activate on a specific block number
                            (for testing)


Attach a REPL to a running Trinity instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can attach a REPL to a running Trinity instance to perform RPC request or
interact with a web3 instance.

.. code-block:: shell

    usage: trinity attach [-h] [ipc_path]
    positional arguments:
        ipc_path    Specify an IPC path
    optional arguments:
        -h, --help  show this help message and exit

Check out the :doc:`Quickstart </guides/quickstart>` for a full example.


Per-module logging
~~~~~~~~~~~~~~~~~~

Trinity provides rich logging output that can be of tremendous help during debugging. By default,
Trinity prints only logs of level ``INFO`` or higher to ``stderr`` and only logs of level ``DEBUG``
or higher to the log file.

This can be adjusted to other log level such as ``ERROR`` or ``DEBUG2`` and independently for both
the ``stderr`` and the file log.

Starting Trinity with ``trinity --log-level DEBUG2`` (shorthand: ``trinity -l DEBUG2``) yields the
absolute maximum of available logging output. However, running Trinity with maximum logging output
might be too overwhelming when we are only interested in logging output for a specific
module (e.g. ``p2p.discovery``).

Fortunately, Trinity allows us to configure logging on a per-module basis by using the
``--log-level`` flag in combination with specific modules and log levels such as in:
``trinity --log-level DEBUG2 --log-level p2p.discovery=ERROR``.

The following table shows various combinations of how to use logging in Trinity effectively.


+---------------------------------------------------------------------+--------------------------------+------------------------------+
| Command                                                             | Stderr log [1]_                | File log [1]_                |
+=====================================================================+================================+==============================+
| ``trinity``                                                         | ``INFO`` [2]_                  | ``DEBUG`` [2]_               |
+---------------------------------------------------------------------+--------------------------------+------------------------------+
| ``trinity --stderr-log-level ERROR``                                | ``ERROR``                      | ``DEBUG``                    |
+---------------------------------------------------------------------+--------------------------------+------------------------------+
| ``trinity --file-log-level INFO``                                   | ``INFO``                       | ``INFO``                     |
+---------------------------------------------------------------------+--------------------------------+------------------------------+
| | ``trinity --file-log-level ERROR``                                | ``ERROR``                      | ``ERROR``                    |
| | ``--stderr-log-level ERROR``                                      |                                |                              |
+---------------------------------------------------------------------+--------------------------------+------------------------------+
| ``trinity --log-level ERROR`` (``trinity -l ERROR``) [3]_           | ``ERROR``                      | ``ERROR``                    |
+---------------------------------------------------------------------+--------------------------------+------------------------------+
| ``trinity --l DEBUG2 -l 'p2p.discovery=ERROR'`` [4]_                | | ``DEBUG2`` but **only**      | | ``DEBUG2`` but **only**    |
|                                                                     | | ``ERROR`` for                | | ``ERROR`` for              |
|                                                                     | | ``p2p.discovery``            | | ``p2p.discovery``          |
+---------------------------------------------------------------------+--------------------------------+------------------------------+
| ``trinity --l ERROR -l 'p2p.discovery=DEBUG2'`` [4]_                | | ``ERROR`` but **also**       | ``ERROR`` [5]_               |
|                                                                     | | ``DEBUG2`` for               |                              |
|                                                                     | | ``p2p.discovery``            |                              |
+---------------------------------------------------------------------+--------------------------------+------------------------------+

.. [1] A stated level e.g. ``DEBUG2`` **always means** that log level **or higher** (e.g. ``INFO``)

.. [2] ``INFO`` is the default log level for the ``stderr`` log, ``DEBUG`` the default log level for the file log.

.. [3] Equivalent to the previous line

.. [4] For per-module configuration, the equal sign (``=``) needs to be used.

.. [5] **Increasing** the per-module log level above the general ``--file-log-level`` is not yet supported
       (See `issue 689 <https://github.com/ethereum/trinity/issues/689>`_ )


Enabling tab completion
~~~~~~~~~~~~~~~~~~~~~~~

Trinity can be configured to auto complete commands when the <tab> key is pressed.

After installing trinity, to activate tab-completion in future bash prompts, use:

.. code:: sh

    register-python-argcomplete trinity >> ~/.bashrc


For one-time activation of argcomplete for trinity, use:

.. code:: sh

    eval "$(register-python-argcomplete trinity)"
