# Empire Find Local Admin Access

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518224039 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/master/lib/modules/powershell/situational_awareness/network/powerview/find_localadmin_access.py |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/discovery/empire_find_local_admin.tar.gz |

## Dataset Description
This dataset represents adversaries using the OpenSCManagerW Win32API call to establish a handle to the remote host and verify if the current user context has local administrator acess to the target.

## Adversary View
```
(Empire: V6W3TH8Y) > usemodule situational_awareness/network/powerview/find_localadmin_access
(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) > info

              Name: Find-LocalAdminAccess
            Module: powershell/situational_awareness/network/powerview/find_localadmin_access
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Finds machines on the local domain where the current user
  has local administrator access. Part of PowerView.

Comments:
  https://github.com/PowerShellMafia/PowerSploit/blob/dev/Reco
  n/

Options:

  Name                    Required    Value                     Description
  ----                    --------    -------                   -----------
  ComputerName            False                                 Hosts to enumerate, comma separated.    
  SearchScope             False                                 Specifies the scope to search under,    
                                                                Base/OneLevel/Subtree (default of       
                                                                Subtree)                                
  ComputerSiteName        False                                 Search computers in the specific AD site
                                                                name, wildcards accepted.               
  Server                  False                                 Specifies an active directory server    
                                                                (domain controller) to bind to          
  Tombstone               False                                 Switch. Specifies that the search should
                                                                also return deleted/tombstoned objects. 
  ComputerOperatingSystem False                                 Searches computers with a specific      
                                                                operating system. Wildcards accepted.   
  ResultPageSize          False                                 Specifies the PageSize to set for the   
                                                                LDAP searcher object.                   
  ComputerDomain          False                                 Specifies the domain to query for       
                                                                computers, defaults to the current      
                                                                domain.                                 
  ComputerSearchBase      False                                 Specifies the LDAP source to search     
                                                                through for computers                   
  ServerTimeLimit         False                                 Specifies the maximum amount of time the
                                                                server spends searching. Default of 120 
                                                                seconds.                                
  ComputerServicePack     False                                 Search computers with a specific service
                                                                pack                                    
  Agent                   True        V6W3TH8Y                  Agent to run module on.                 
  CheckShareAccess        False                                 Switch. Only display found shares that  
                                                                the local user has access to.           
  ComputerLDAPFilter      False                                 Specifies an LDAP query string that is  
                                                                used to search for computer objects.    

(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) > execute
[*] Tasked V6W3TH8Y to run TASK_CMD_JOB
[*] Agent V6W3TH8Y tasked with task ID 11
[*] Tasked agent V6W3TH8Y to run module powershell/situational_awareness/network/powerview/find_localadmin_access
(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) > Job started: X3U8SY
HFDC01.shire.com
IT001.shire.com

Find-LocalAdminAccess completed!

(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/discovery/empire_find_local_admin.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT channel, COUNT(1)
FROM mordorTable
GROUP BY channel
    '''
)
df.show(10,False)
        