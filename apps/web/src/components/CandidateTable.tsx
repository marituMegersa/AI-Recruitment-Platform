import React from 'react';

export function CandidateTable({ records }: { records: any[] }) {
  return (
    <div style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>📊 Candidate Evaluation Directory</h3>
      {records.length === 0 ? (
        <p style={{ color: '#64748b', fontSize: '14px' }}>No candidate evaluations recorded yet.</p>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '14px' }}>
          <thead>
            <tr style={{ background: '#f8fafc', textAlign: 'left', borderBottom: '2px solid #e2e8f0' }}>
              <th style={{ padding: '0.75rem' }}>Name</th>
              <th style={{ padding: '0.75rem' }}>Match Score</th>
              <th style={{ padding: '0.75rem' }}>Status</th>
              <th style={{ padding: '0.75rem' }}>Matched Skills</th>
            </tr>
          </thead>
          <tbody>
            {records.map((r, i) => (
              <tr key={i} style={{ borderBottom: '1px solid #e2e8f0' }}>
                <td style={{ padding: '0.75rem', fontWeight: 'bold' }}>{r.candidate_name}</td>
                <td style={{ padding: '0.75rem' }}>{r.match_score}%</td>
                <td style={{ padding: '0.75rem' }}>
                  <span style={{ padding: '0.25rem 0.5rem', borderRadius: '4px', background: r.screening_status === 'RECOMMENDED' ? '#dcfce7' : '#fef3c7', color: r.screening_status === 'RECOMMENDED' ? '#15803d' : '#b45309', fontWeight: 'bold', fontSize: '12px' }}>
                    {r.screening_status}
                  </span>
                </td>
                <td style={{ padding: '0.75rem' }}>{Array.isArray(r.matched_skills) ? r.matched_skills.join(', ') : 'Python, FastAPI'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
